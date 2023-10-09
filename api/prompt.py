import os

chat_language = os.getenv("INIT_LANGUAGE", default = "zh")

MSG_LIST_LIMIT = int(os.getenv("MSG_LIST_LIMIT", default = 7))
LANGUAGE_TABLE = {
  "zh": "哈囉！",
  "en": "Hello!"
}

class Prompt:
    def __init__(self):
        self.msg_list = []
        self.msg_list.append({"role": "system", "content": f"{LANGUAGE_TABLE[chat_language]}, 你是一個AI助教，會代替老師初步回答問題，如果有需要會提醒學生跟老師確認"})
            # f"AI:{LANGUAGE_TABLE[chat_language]}")
    
    def add_msg(self, new_msg):
        if len(self.msg_list) >= MSG_LIST_LIMIT:
            self.remove_msg()
        self.msg_list.append({"role": "user", "content": new_msg})

    def remove_msg(self):
        self.msg_list.pop(0)

    def generate_prompt(self):
        # return '\n'.join(self.msg_list)
        return self.msg_list