class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def justify(arr, mid_padding, end_padding):
            result.append(mid_padding.join(arr) + end_padding)

        def padding_data(left_over_space, spaces):
            return (left_over_space // spaces) + 1, left_over_space % spaces

        def add_extra_padding(arr, epc):
            for i in range(1, epc + 1):
                arr[i] = " " + arr[i]
            return arr

        def create_text(arr, l, is_last):
            nonlocal result

            left_over_space = maxWidth - l
            spaces = len(arr) - 1

            if not spaces or is_last:
                justify(arr, " ", " " * left_over_space)
            else:

                pfa, epc = padding_data(left_over_space, spaces)
                arr = add_extra_padding(arr, epc)
                justify(arr, " " * pfa, "")

        result = []
        i, N, sfs, worker = 1, len(words), len(words[0]), [words[0]]

        while i < N:
            next_word = words[i]
            next_word_len = len(next_word) + 1

            if sfs + next_word_len > maxWidth:
                create_text(worker, sfs, False)
                sfs, worker = next_word_len - 1, [next_word]
            else:
                sfs += next_word_len
                worker.append(next_word)
            i += 1

        create_text(worker, sfs, True)
        return result
        