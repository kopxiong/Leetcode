# We are given a list cpdomains of count-paired domains.
# We would like a list of count-paired domains,
# (in the same format as the input, and in any order),
# that explicitly counts the number of visits to each subdomain.

import collections

class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        ## 01. Using dict
        # result = {}
        # for item in cpdomains:
        #     value, domain = item.split()
        #     subdomains = domain.split('.')
        #     keys = ['.'.join(subdomains[i:]) for i in range(len(subdomains))]
        #
        #     for k in keys:
        #         result[k] = result.get(k, 0) + int(value)
        #
        # return ['%s %s' % (v, k) for k, v in result.items()]

        ## 02. Using hash table
        result = collections.Counter()
        for item in cpdomains:
            value, domain = item.split()
            value = int(value)
            subdomains = domain.split('.')

            for i in range(len(subdomains)):
                result['.'.join(subdomains[i:])] += value

        return ['%s %s' % (v, k) for k, v in result.items()]

if __name__ == "__main__":
    cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]

    print(Solution().subdomainVisits(cpdomains))
