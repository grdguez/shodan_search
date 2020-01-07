import shodan

SHODAN_API_KEY = "YOUR_SHODAN_API_KEY_HERE"

api = shodan.Shodan(SHODAN_API_KEY)

try:
        # Search Shodan
        results = api.search('SHODAN_SEARCH_HERE(EX: yawncam)')

        # Show the results
        for result in results['matches']:
                print('%s' % result['ip_str'])
except shodan.APIError as e:
        print ('Error: %s' % e)
