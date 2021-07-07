import random

lines = open('in/user-agents.txt').read().splitlines()

# user_agent = random.choice(lines)

# def readFile(fileName):
#     fileObj = open(fileName, "r")  # opens the file in read mode
#     words = fileObj.read().splitlines() # puts the file into an array
#     fileObj.close()
#     return words
#




def get_user_agents():
    # url = 'https://developers.whatismybrowser.com/useragents/explore/software_name/chrome/'
    pass
    # response = requests.get(url)
    # parser = fromstring(response.text)
    # user_agents = set()
    # for i in parser.xpath('//tbody/tr')[:20]:
    #     if i.xpath('.//td[5][contains(text(),"Very common")]'):
    #         user_agent = str(i.xpath('//a[@class="useragent"]/text()'))
    #         user_agents.add(user_agent)
    # return user_agents

# user_agents = get_user_agents()
#
# # user_agents_pool =cycle(user_agents)
# # user = next(user_agents_pool)
# print(user_agents[2])