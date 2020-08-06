import time
list_words = ['hello', ' day', 'love', 'good', 'hi']

response = {
    'hello': 'hi dear, how are you today',
    'day': 'going well thank you',
    'love': 'thanks',
    'doing good': 'am also doing good, and nice to know'
}
user_input = input('chat with our chat bot :\n ')
while len(user_input) > 0:
    if list_words[0] in user_input or list_words[4] in user_input:
        print('response processing')
        time.sleep(2)
        print(response['hello'])
    elif list_words[1] in user_input:
        print('response processing')
        time.sleep(2)
        print(response['day'])
    elif list_words[2] in user_input:
        print('response processing')
        time.sleep(2)
        print(response['love'])
    elif list_words[3] in user_input:
        print('response processing')
        time.sleep(2)
        print(response['doing good'])
    elif user_input == 'exit':
        print('pleasure talking to you, hope to talk to you next time')
        time.sleep(2)
        exit()
    elif 'can' and 'question' in user_input:
        print('response processing')
        time.sleep(2)
        print('you can ask your question')
    elif 'question' in user_input and 'can' not in user_input:
        print('response processing')
        time.sleep(2)
        print('sorry am just a bolt but our customer care can assist you better, contact them on 09090240674')
    else:
        print("sorry i don't have a response for that question")
    user_input = input()
