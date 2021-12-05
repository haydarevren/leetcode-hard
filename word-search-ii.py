# 212. Word Search II
# https://leetcode.com/problems/word-search-ii/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = None

class Trie:
    def __init__(self):
        self.root=TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isEnd = word 

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def builtTrie(words): #built trie   
            trie = Trie()
            for w in words:
                trie.insert(w)      
            return trie

        def is_valid_word(path_board,path_trie):
            return path_trie[-1].isEnd
        
        def get_candidate_moves(path_board,path_trie):        
            moves= ((1,0),(0,1),(-1,0),(0,-1))
            candidates=[]
            i,j = path_board[-1]
            cur = path_trie[-1]
            
            for move in moves:
                #check if path is valid and a child node in trie
                x, y =  i+move[0], j+move[1]
                if x<0 or x>m-1 or y<0 or y>n-1 or \
                [x,y] in path_board or \
                board[x][y] not in cur.children:
                    continue     
                candidates.append([x,y])
            return candidates
        
        def search(path_board,path_trie,output):
            if is_valid_word(path_board,path_trie):
                output.add(is_valid_word(path_board,path_trie))
                    
            for candidate in get_candidate_moves(path_board,path_trie):
                path_board.append(candidate)
                path_trie.append(path_trie[-1].children[board[candidate[0]][candidate[1]]])
                search(path_board,path_trie,output)
                path_board.pop()
                path_trie.pop()
        
        words = set(words)
        #built trie
        
        trie = builtTrie(words)
        
        output=set()
        m = len(board)
        n = len(board[0]) 
        
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie.root.children:
                    path_board = [[i,j]]
                    path_trie = [trie.root.children[board[i][j]]]
                    oldsize = len(output)
                    search(path_board,path_trie,output)
                    if oldsize!= len(output):
                        words = words - output
                        #built trie 
                        trie = builtTrie(words)

        return list(output)
        
