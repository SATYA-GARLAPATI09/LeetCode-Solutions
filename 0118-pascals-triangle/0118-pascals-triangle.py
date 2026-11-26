class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        def ansRow(num: int) -> list[int]:
            row = [1]
            ans = 1
            for i in range(1, num + 1):
                ans = ans * (num - i + 1) // i
                row.append(ans)
            return row

        answer = []
        for r in range(numRows):
            answer.append(ansRow(r))
        return answer

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna