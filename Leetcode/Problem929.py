class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        s = set() 

        for email in emails: 
            beginning, end = email.split("@")
            new_beginning = beginning.split("+")[0].replace(".", "")
            s.add(new_beginning + end)
        
        return len(s)