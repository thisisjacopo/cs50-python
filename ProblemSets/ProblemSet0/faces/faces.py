def main():
    sentence = input("Hey there!:) Please enter a sentence containing some emoticons: ")
    print(convert(sentence))   
    
#function that converts emoticons into emojis
def convert(sentence: str):
    sentence = sentence.replace(":)", "🙂")
    sentence = sentence.replace(":(", "🙁")
    return sentence

main()