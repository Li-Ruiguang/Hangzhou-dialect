import random
import hashlib

# 定义变量选项（古吉拉特语）
locations = ["ગામડું", "બાગ", "પર્વત", "નદીકાંઠો", "ચા દુકાન", "શહેરની ગલી", "બસ સ્ટોપ"]
times = ["સવાર", "બપોર", "સાંજ", "રાત્રિ", "મધ્યરાત્રિ"]
weather_conditions = ["વરસાદી", "ધુપાળુ", "વીજળીવાળું", "ધુમ્મસ", "હિમવર્ષા", "જોરદાર પવન"]
relationships = ["પડોશી", "સહકર્મી", "પતિ-પત્ની", "ભાઇ-બહેન", "મિત્રો", "અજાણ્યા લોકો"]
motivations = [
    "આજના દિવસે ખેતર માટે યોગ્ય છે કે નહીં તે ચર્ચા કરવી",
    "હવામાન વિશે ચાલતાં ચાલતાં વાત કરવી",
    "પર્વત પર ચાલવાનું ચાલુ રાખવું કે પાછા ફરવું તે નક્કી કરવું",
    "આવતીકાલના પ્રવાસ માટે યોજના બનાવવી",
    "મોસમના પરિવર્તનનો જીવન પર થતો અસર ચર્ચાવવી",
    "એક ખાસ હવામાન અનુભવ યાદ કરવો"
]

# 定义对话模板
dialog_templates = [
    [
        "A: આજે હવામાન {weather} છે. તમે શું વિચારો છો?",
        "B: હા, {weather} હવામાન ખરેખર {location} માટે યોગ્ય છે.",
        "A: હું હમણાં જ વિચારતો હતો કે {motivation}.",
        "B: હા, ચોક્કસ! તમે {time} માટે કોઈ ખાસ તૈયારી કરી છે?",
        "A: હા, હું {additional} લેવા જઇશ.",
        "B: સારું વિચાર્યું! ચાલો, તે પછી શરૂ કરીએ."
    ],
    [
        "A: {location} પર આ હવામાન કેટલું સુંદર લાગે છે!",
        "B: હા, હવામાન {weather_feeling} છે. તમે આ મોસમમાં શું કરવા પસંદ કરો છો?",
        "A: હું સામાન્ય રીતે {activity} કરું છું. તમે呢?",
        "B: હું પણ એજ કરું છું, પણ ક્યારેક હું {activity} કરવી પસંદ કરું છું.",
        "A: આ મોસમમાં આપણે મળીને કંઈક તાજું કરીશું?",
        "B: ચોક્કસ! એ માટે હું ઇચ્છુક છું."
    ]
]

# 生成唯一标识符
def generate_unique_id(context):
    context_str = f"{context['location']}-{context['time']}-{context['weather']}-{context['relationship']}-{context['motivation']}"
    return hashlib.md5(context_str.encode()).hexdigest()

# 随机生成对话
def generate_conversation():
    location = random.choice(locations)
    time = random.choice(times)
    weather = random.choice(weather_conditions)
    relationship = random.choice(relationships)
    motivation = random.choice(motivations)
    dialog_template = random.choice(dialog_templates)
    
    # 填充模板
    dialog = [line.format(
        location=location,
        time=time,
        weather=weather,
        motivation=motivation,
        weather_feeling=random.choice(["મજેદાર", "ઉષ્માગ્રસ્ત", "ઠંડું", "આનંદદાયક"]),
        activity=random.choice(["ચમન", "વાંચન", "ચા પીવી", "ગપશપ", "ફોટોગ્રાફી"]),
        additional=random.choice(["સુરક્ષિત રહેવું", "છત્રી સાથે રાખવી", "યોગ્ય કપડાં પહેરવાં"])
    ) for line in dialog_template]

    context = {
        "location": location,
        "time": time,
        "weather": weather,
        "relationship": relationship,
        "motivation": motivation,
        "dialog": dialog
    }
    context["unique_id"] = generate_unique_id(context)
    return context

# 生成Markdown文件
def generate_markdown(conversations, filename="weather_conversations_gujarati.md"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write("# હવામાન વિષયક સંવાદ (ગુજરાતી ભાષા)\n\n")
        for i, convo in enumerate(conversations):
            f.write(f"## સંવાદ ઉદાહરણ {i + 1}\n")
            f.write("**પ્રસંગ**:\n")
            f.write(f"- સ્થાન: {convo['location']}\n")
            f.write(f"- સમય: {convo['time']}\n")
            f.write(f"- હવામાન: {convo['weather']}\n")
            f.write(f"- સંબંધ: {convo['relationship']}\n")
            f.write(f"- ચર્ચાવિષય: {convo['motivation']}\n\n")
            f.write("**સંવાદ**:\n")
            f.write("```\n")
            for line in convo["dialog"]:
                f.write(line + "\n")
            f.write("```\n\n")
            f.write("---\n\n")

# 主函数
def main():
    num_conversations = 500  # 生成500组对话
    conversations = []
    unique_ids = set()  # 用于存储唯一标识符，避免重复

    while len(conversations) < num_conversations:
        convo = generate_conversation()
        if convo["unique_id"] not in unique_ids:  # 检查是否重复
            unique_ids.add(convo["unique_id"])
            conversations.append(convo)

    generate_markdown(conversations)
    print(f"500 સંવાદો તૈયાર છે અને 'weather_conversations_gujarati.md' ફાઇલમાં સંગ્રહિત છે.")

if __name__ == "__main__":
    main()