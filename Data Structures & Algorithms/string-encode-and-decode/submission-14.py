class Solution:

    def encode(self, strs: List[str]) -> str:
        prefix = ""
        for string in strs:
            prefix += str(len(string)) + ","
        return prefix + "#" + "".join(strs)
    def decode(self, s: str) -> List[str]:
        output = []
        prefix, string = s.split("#", 1)
        last_index = 0
        for length in prefix.split(","):
            if not length:
                continue

            output.append(string[last_index:last_index + int(length)])
            last_index += int(length)
        return output
