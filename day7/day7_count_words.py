def count_words(sentence):
    words = sentence.split()
    return len(words)

sentence = input("문장을 입력하세요: ")
print(f"총 {count_words(sentence)}개의 단어가 있습니다.")

