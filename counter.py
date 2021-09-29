from collections import Counter, defaultdict, OrderedDict

text = 'hello world'

# top 5 most occurrence chars in alphabetical order. output:lodeh


def text_counter_using_collection(input_text):
    res = defaultdict(list)

    for key, val in sorted(dict(Counter(list(input_text.replace(' ', ''))).most_common()).items()):
        res[val].append(key)

    result = OrderedDict(sorted(res.items(), key=lambda t: t[0], reverse=True))

    res_set = list()
    for k, v in result.items():
        res_set += v

    print(''.join(res_set)[0:5])


def text_counter_simple(input_text):
    counter_chars = dict()
    for char in input_text.replace(' ', ''):
        if char in counter_chars.keys():
            counter_chars[char] += 1
        else:
            counter_chars[char] = 1

    g_arr = dict()

    for k, v in sorted(counter_chars.items()):
        if v in g_arr.keys():
            g_arr[v].append(k)
        else:
            g_arr[v] = [k]

    sorted_arr = sorted(g_arr.items(), key=lambda item: item[0], reverse=True)
    res_set = list()
    for k, v in sorted_arr:
        res_set += v

    print(''.join(res_set[0:5]))


if __name__ == '__main__':

    # import timeit

    text_counter_using_collection(text)
    text_counter_simple(text)

    # print(timeit.timeit("text_counter_using_collection(text)", globals=locals()))
    # print(timeit.timeit("text_counter_simple(text)", globals=locals()))

    # fn text_counter_simple is faster
