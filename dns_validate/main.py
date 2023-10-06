import aiohttp
import aiodns
import asyncio

OUTPUT_FILE = "resolvers.txt"
URL = "https://public-dns.info/nameservers.txt"
TRUSTED_RESOLVERS = ['8.8.8.8', '1.1.1.1']  # Google and Cloudflare DNS
TRUSTED_DOMAINS = ['google.com', 'amazon.com', 'microsoft.com']


async def fetch_dns_list(session):
    async with session.get(URL) as response:
        return await response.text()


async def validate_dns(dns):
    for trusted_resolver in TRUSTED_RESOLVERS:
        resolver = aiodns.DNSResolver(nameservers=[trusted_resolver])
        try:
            # Check multiple trusted domains
            for domain in TRUSTED_DOMAINS:
                await asyncio.wait_for(resolver.query(domain, 'A'), timeout=5)
        except asyncio.TimeoutError:
            print(f"DNS {dns} timed out")
            return (dns, False)
        except Exception as e:
            print(f"DNS {dns} is invalid due to {e}")
            return (dns, False)
    return (dns, True)


async def async_main():
    async with aiohttp.ClientSession() as session:
        dns_list = await fetch_dns_list(session)
        dns_servers = dns_list.strip().split("\n")

        # Validate DNS servers concurrently
        results = await asyncio.gather(*(validate_dns(dns) for dns in dns_servers))

        # Write results to file
        with open(OUTPUT_FILE, 'w') as f:
            for dns, is_valid in results:
                if is_valid:
                    f.write(f"{dns}\n")

        print(f"Results written to {OUTPUT_FILE}")


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(async_main())
    loop.close()


if __name__ == "__main__":
    main()
