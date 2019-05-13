from collections import defaultdict

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        # opted for defaultdict over counter here
        
        freq = defaultdict(int)
        for cpd in cpdomains:
            tokens = cpd.split(" ")
            count = int(tokens[0])
            domains = tokens[1].split(".")
        
            for i in range(len(domains)):
                domain = ""
                for j in range(i, len(domains)):
                    domain += domains[j]
                    if j < len(domains) - 1:
                        domain += "."
                freq[domain] += count
        
        # generating output string format from dict of counts
        output = []
        for domain, count in freq.items():
            output.append("" + str(count) + " " + domain)
        return output