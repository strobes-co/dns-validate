import aiohttp
import aiodns
import asyncio

OUTPUT_FILE = "resolvers.txt"
URL = "https://public-dns.info/nameservers.txt"


async def fetch_dns_list(session):
    async with session.get(URL) as response:
        return await response.text()


async def validate_dns(dns):
    resolver = aiodns.DNSResolver(nameservers=[dns])
    try:
        await resolver.query('google.com', 'A')
        return (dns, True)
    except Exception as e:
        print(f"DNS {e} is invalid")
        return (dns, False)


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
