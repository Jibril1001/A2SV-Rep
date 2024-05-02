class Solution:
    def interpret(self, command: str) -> str:
        ans=command
        return ans.replace("()","o").replace("(al)","al")