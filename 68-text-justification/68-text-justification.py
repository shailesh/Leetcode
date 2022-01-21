class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # round robin for distributing spaces
        res, cur = [], []
        num_letters = 0 
        for w in words:
            # if there isn't enough space this word
            # num_letters + num_spaces + len_w
            if num_letters + len(cur) + len(w) > maxWidth:
                # round robin for spaces
                for i in range(maxWidth - num_letters):
                    num_interval = len(cur) - 1
                    if num_interval == 0:
                        cur[0] += ' '
                    else:
                        cur[i % num_interval] += ' '
                res.append(''.join(cur))
                cur, num_letters = [], 0
            cur.append(w)
            num_letters += len(w)
        final_row = ' '.join(cur).ljust(maxWidth)
        return res + [final_row]
        