# row, column = input().split(' ')
# words = []
# input_list = [input() for _ in range((int(row)))]

# for row in input_list:
#     words += [w for w in row.split('#') if len(w) >= 2]
    
# for col in zip(*input_list):
#     col_string = ''.join(col)
#     words += [w for w in col_string.split('#') if len(w) >= 2]
        
# print(min(words))

#--------------------#
# from collections import defaultdict
# N, B = input().split(' ')
# A = list(map(int, input().split()))

# balance = 0
# count = 0
# prefix_count = defaultdict(int)
# prefix_count[0] = 1  
# found_B = False

# for num in A:
#     if num < int(B):
#         balance -= 1
#     elif num > int(B):
#         balance += 1
#     else:
#         found_B = True

#     if found_B:
#         count += prefix_count[balance]
#     else:
#         prefix_count[balance] += 1

# print(count)

#-----------------#
# N = int(input())

# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
# C = list(map(int, input().split()))


# intersection = []

# for i in A:
#     if i in B and i in C:
#         intersection.append(i)

# count = []

# duplicates = []
# seen = set()
# for event in A:
#     if event not in intersection:
#         count.append(event)
#     if A.count(event) > 1 and event not in seen:
#         duplicates.append(event)
#         seen.add(event)

# for event in B:
#     if event not in intersection:
#         count.append(event)
#     if B.count(event) > 1 and event not in seen:
#         duplicates.append(event)
#         seen.add(event)

# for event in C:
#     if event not in intersection:
#         count.append(event)
#     if A.count(event) > 1 and event not in seen:
#         duplicates.append(event)
#         seen.add(event)
# for x in seen:
#     count.append(x) 

# print(len(set(count)))

#-------------------#

# def longest_common_prefix(s1, s2):
#     min_len = min(len(s1), len(s2))
#     for i in range(min_len):
#         if s1[i] != s2[i]:
#             return i
#     return min_len

# def solve():
#     N = int(input())
#     database = [input().strip() for _ in range(N)]
#     Q = int(input()) 
#     queries = [input().strip() for _ in range(Q)]
    
#     for query in queries:
#         total_actions = 0
#         for word in database:
#             lcp_length = longest_common_prefix(query, word)
#             total_actions += 1 + lcp_length 
#             if query == word:
#                 break 
        
#         print(total_actions)

# solve()


# MOD = 10**9 + 7

# def count_ways(N, seq):
#     dp = [[0] * (N + 1) for _ in range(N + 1)]
#     dp[0][0] = 1  

#     for i in range(N):
#         for j in range(N + 1):
#             if dp[i][j] == 0:
#                 continue
#             if seq[i] == "?":
#                 if j + 1 <= N:
#                     dp[i + 1][j + 1] = (dp[i + 1][j + 1] + dp[i][j]) % MOD
#                 if j - 1 >= 0: 
#                     dp[i + 1][j - 1] = (dp[i + 1][j - 1] + dp[i][j]) % MOD
#             elif seq[i] == "(":
#                 if j + 1 <= N:
#                     dp[i + 1][j + 1] = (dp[i + 1][j + 1] + dp[i][j]) % MOD
#             elif seq[i] == ")":
#                 if j - 1 >= 0:
#                     dp[i + 1][j - 1] = (dp[i + 1][j - 1] + dp[i][j]) % MOD
#             elif seq[i] == "[":
#                 if j + 1 <= N:
#                     dp[i + 1][j + 1] = (dp[i + 1][j + 1] + dp[i][j]) % MOD
#             elif seq[i] == "]":
#                 if j - 1 >= 0:
#                     dp[i + 1][j - 1] = (dp[i + 1][j - 1] + dp[i][j]) % MOD
#             elif seq[i] == "{":
#                 if j + 1 <= N:
#                     dp[i + 1][j + 1] = (dp[i + 1][j + 1] + dp[i][j]) % MOD
#             elif seq[i] == "}":
#                 if j - 1 >= 0:
#                     dp[i + 1][j - 1] = (dp[i + 1][j - 1] + dp[i][j]) % MOD

#     return dp[N][0]

# N = int(input())
# seq = input()

# print(count_ways(N, seq))

# def longest_common_prefix(s1, s2):
#     min_len = min(len(s1), len(s2))
#     for i in range(min_len):
#         if s1[i] != s2[i]:
#             return i
#     return min_len

# def solve():
#     N = int(input())
#     database = [input().strip() for _ in range(N)]
#     Q = int(input()) 
#     queries = [input().strip() for _ in range(Q)]
    

#     lcp_matrix = [[0] * N for _ in range(N)]  
#     for i in range(N):
#         for j in range(i + 1, N):
#             lcp_len = longest_common_prefix(database[i], database[j])
#             lcp_matrix[i][j] = lcp_len
#             lcp_matrix[j][i] = lcp_len 

#     for query in queries:
#         total_actions = 0
#         for word in database:
#             lcp_length = longest_common_prefix(query, word)
#             total_actions += 1 + lcp_length  
#             if query == word:
#                 break 
        
#         print(total_actions)

# solve()
# def longest_common_prefix(s1, s2):
#     min_len = min(len(s1), len(s2))
#     for i in range(min_len):
#         if s1[i] != s2[i]:
#             return i
#     return min_len

# def solve():
#     N = int(input())
#     database = [input().strip() for _ in range(N)]
#     Q = int(input()) 
#     queries = [input().strip() for _ in range(Q)]

#     for query in queries:
#         total_actions = 0
#         for word in database:
#             lcp_length = longest_common_prefix(query, word)
#             total_actions += 1 + lcp_length
#             if query == word:
#                 break 
        
#         print(total_actions)

# solve()
# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.is_end_of_word = False

# class Trie:
#     def __init__(self):
#         self.root = TrieNode()

#     def insert(self, word):
#         node = self.root
#         for char in word:
#             if char not in node.children:
#                 node.children[char] = TrieNode()
#             node = node.children[char]
#         node.is_end_of_word = True


#     def longest_common_prefix(self, query, word):
#         min_len = min(len(query), len(word))
#         for i in range(min_len):
#             if query[i] != word[i]:
#                 return i
#         return min_len

# def solve():
#     N = int(input())
#     database = [input().strip() for _ in range(N)]
#     Q = int(input())
#     queries = [input().strip() for _ in range(Q)]

#     trie = Trie()

#     for word in database:
#         trie.insert(word)

#     for query in queries:
#         total_actions = 0
#         for word in database:
#             lcp_length = trie.longest_common_prefix(query, word)
#             total_actions += 1 + lcp_length 
#             if query == word:
#                 break
        
#         print(total_actions)

# solve()
def main():
    # Input
    a, b, c, d = map(int, input().split())

    # Sorting the segments
    if a > b:
        a, b = b, a
    if c > d:
        c, d = d, c
    
    # Ensuring a >= b >= c >= d
    if a > c:
        a, c = c, a
        b, d = d, b

    # Output based on the conditions
    if c - b >= 0:
        print(b - a + d - c)
    elif d < b:
        print(b - a)
    else:
        print(d - a)

# Call the function to execute the logic
main()
