import streamlit as st

# 페이지 제목
st.title("용감한 나무늘보 뚜뚜: 동화책 제작 보고")
st.markdown("**작성자**: 이희근")
st.markdown("**날짜**: 2024.09.28")

# 1. 동화책 개요
st.header("1. 동화책 개요")
st.markdown("""
**제목**: 용감한 나무늘보 뚜뚜  
**대상 독자**: 초등학교 저학년  
**주제**: 느리지만 신중한 나무늘보 뚜뚜가 숲속 친구들을 도우며 용기와 우정을 쌓아가는 이야기  
**교훈**: 빠르기보다는 신중함과 마음씨가 더 중요하다는 것을 강조하며, 친구들을 돕는 따뜻한 마음을 키워줌.
""")

# 2. 주요 내용
st.header("2. 주요 내용")
st.markdown("""
**주인공**: 나무늘보 ‘뚜뚜’  
**주요 등장인물**: 다람쥐, 뱀, 숲속의 여러 동물들  
**배경**: 숲속에서 벌어지는 사건과 폭풍의 위협  
**주요 사건**: 폭풍이 닥쳐오는 상황에서 숲속 동물들이 뚜뚜의 도움을 받아 위기에서 벗어남.
""")

# 3. 그림 구성과 설명 (탭 형태로 구현)
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["1컷: 숲속 생활", "2컷: 다가오는 폭풍", "3컷: 뚜뚜가 다람쥐를 구출", "4컷: 뱀을 구출", "5컷: 폭풍 후 감사", "6컷: 뚜뚜의 칭찬"])

with tab1:
    st.image("/Users/dasepa/R coding/streamlit_test/myenv/share/jupyter/cut1-1.webp", width=500)
    st.markdown("""
    **스크립트**: 깊은 숲속에 나무늘보 뚜뚜가 살고 있었어요. 뚜뚜는 항상 느릿느릿 움직였어요.  
    친구들은 뚜뚜를 보며 "뚜뚜야, 너는 정말 느리구나!"라고 말했지만, 뚜뚜는 기분 나빠하지 않았어요.  
    "난 느리지만, 내가 할 수 있는 게 있어!"라고 스스로를 다독였거든요.
    
    **그림 설명**: 뚜뚜는 숲속을 평화롭게 즐기고 있는 장면.
    """)

with tab2:
    st.image("/Users/dasepa/R coding/streamlit_test/myenv/share/jupyter/cut2-1.webp", width=500)
    st.markdown("""
    **스크립트**: 어느 날, 커다란 폭풍이 다가오고 있다는 소식이 들렸어요.  
    모든 동물들은 서둘러 안전한 곳을 찾기 시작했지만, 뚜뚜는 느려서 빨리 움직일 수 없었어요.
    **그림 설명**: 다람쥐는 무서워하고, 뚜뚜는 천천히 움직이는 장면.
    """)

with tab3:
    st.image("/Users/dasepa/R coding/streamlit_test/myenv/share/jupyter/cut3-1.webp", width=500)
    st.markdown("""
    **스크립트**: 다람쥐가 나무 위에서 울고 있었어요. 뚜뚜가 다람쥐를 도와 조심스럽게 내려줍니다.
    **그림 설명**: 뚜뚜가 느리지만 신중하게 다람쥐를 구출하는 장면.
    """)

with tab4:
    st.image("/Users/dasepa/R coding/streamlit_test/myenv/share/jupyter/cut4-1.webp", width=500)
    st.markdown("""
    **스크립트**: 뱀이 꼬리가 돌에 걸려 움직이지 못하는 것을 본 뚜뚜가 신중하게 돌을 치워줍니다.
    **그림 설명**: 뚜뚜가 신중하게 뱀을 구출하는 장면.
    """)

with tab5:
    st.image("/Users/dasepa/R coding/streamlit_test/myenv/share/jupyter/cut5-1.webp", width=500)
    st.markdown("""
    **스크립트**: 폭풍이 지나가고, 동물들은 뚜뚜에게 감사의 인사를 전합니다.
    **그림 설명**: 동물들이 뚜뚜에게 감사하는 장면.
    """)

with tab6:
    st.image("/Users/dasepa/R coding/streamlit_test/myenv/share/jupyter/cut6-1.webp", width=500)
    st.markdown("""
    **스크립트**: 뚜뚜는 부끄럽게 웃으며 친구들에게 칭찬을 받습니다.
    **그림 설명**: 동물들이 뚜뚜를 칭찬하며 기뻐하는 장면.
    """)

# 4. 교훈 및 메시지
st.header("4. 교훈 및 메시지")
st.markdown("""
- **교훈**: 동화는 빠르기만을 중요시하지 않고, 느림 속에서도 타인을 돕고 자신만의 속도로 세상을 헤쳐나가는 용기를 강조합니다.
- **전달 메시지**: "빠르지 않아도 괜찮아, 중요한 건 친구를 돕고 함께하는 마음이야."
""")

# 5. 기대 효과
st.header("5. 기대 효과")
st.markdown("""
- **독자 반응**: 초등학교 저학년 독자들은 뚜뚜의 느림 속에서도 보여주는 용기와 따뜻함을 통해 친구와의 우정과 배려심을 배울 수 있습니다.
- **교육적 효과**: 아이들에게 신중함의 중요성과 타인을 돕는 배려심을 강조하여 정서 발달에 도움을 줍니다.
""")

# 6. 결론
st.header("6. 결론")
st.markdown("""
"용감한 나무늘보 뚜뚜"는 어린 독자들이 느림의 가치를 배우고, 타인을 돕는 즐거움을 경험할 수 있는 동화책입니다.
""")