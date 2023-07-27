import asyncio
import time

import openai
import subprocess
import os
import stat

OPENAI_KEY = ""
APP_FILE_NAME = "test.py"
REQS_FILE_NAME = "requirements_doc.txt"


def setup():
    openai.api_key = OPENAI_KEY
    # print(openai.Model.list())


async def generate_application():
    index = 1
    while True:
        try:
            print("Iteration:", index)
            req_str = None
            with open(REQS_FILE_NAME, "r") as file:
                req_str = file.read()
                file.close()

            if req_str is None:
                print("req_str is None")
                exit(-1)

            code_str = None
            with open(APP_FILE_NAME, "r") as file:
                code_str = "iterate on the following program: " + file.read()
                file.close()

            content_str = req_str + "\n" + code_str

            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-16k",
                messages=[
                    {"role": "system", "content": "You are an expert python developer"},
                    {"role": "user", "content": content_str},
                ]
            )

            content = str(completion.choices[0].message.content)
            start = content.find("")
            end = content.rindex("")
            code = content[start:end]

            with open(APP_FILE_NAME, "w") as file:
                file.write(code)
                file.close()
                os.chmod(APP_FILE_NAME, stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR | stat.S_IRGRP | stat.S_IROTH)

            print("Start subprocess")
            subprocess.run(
                ['python3', APP_FILE_NAME],
                shell=False,
                check=True,
                capture_output=True,
                text=True,
                encoding="utf-8"
            )
            print("Ended subprocess")
            index += 1

        except Exception as error:
            print("Caught error")
            if type(error) is openai.error.RateLimitError:
                print("Rate limit error, taking a 1 minute break")
                time.sleep(60)
            else:
                with open(REQS_FILE_NAME, "r+") as file:
                    err_str = error.stderr.split('\n')[-2]
                    location = file.read().find(err_str)
                    if location == -1:
                        file.write("\n" + err_str)
                    file.close()
            index += 1


def get_reqs_as_json():
    return


async def main():
    setup()
    await generate_application()


if __name__ == '__main__':
    asyncio.run(main())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
