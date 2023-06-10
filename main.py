import streamlit as st

from annotated_text import annotated_text

from model.model_Ner1.nermodel1 import text_to_token


path = ''
text = st.text_input('Text', '')
y_predicts =  text_to_token([text],path)
# print(y_predicts['taget'])
st.write('The current movie title is',y_predicts)

# x =  
# x = x + "quoc"

# annotated_text(y_predicts)
# annotated_text(
#     "This mas ",
#     ("is", "verb"),
#     " some ",
#     ("annotated", "adj"),
#     ("text", "noun"),
#     " for those of ",
#     ("you", "pronoun"),
#     " who ",
#     ("like", "verb"),
#     " this sort of ",
#     ("thing", "noun"),
#     "."
# )