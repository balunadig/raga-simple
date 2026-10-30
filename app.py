import streamlit as st

st.set_page_config(page_title="Raga Finder", page_icon="🎵")

RAGAS = {
    "Yaman": {"aaroh": "N R G M# D N S'", "avroh": "S' N D P M# G R S", "time": "Evening", "thaat": "Kalyan", "mood": "Devotional, Peaceful"},
    "Bhairav": {"aaroh": "S r G M P d N S'", "avroh": "S' N d P M G r S", "time": "Morning", "thaat": "Bhairav", "mood": "Serious, Devotional"},
    "Malkauns": {"aaroh": "S g M d n S'", "avroh": "S' n d M g S", "time": "Midnight", "thaat": "Bhairavi", "mood": "Meditative, Intense"},
    "Bhairavi": {"aaroh": "S r g M P d n S'", "avroh": "S' n d P M g r S", "time": "Morning", "thaat": "Bhairavi", "mood": "Devotional, Emotional"},
    "Kafi": {"aaroh": "S R g M P D n S'", "avroh": "S' n D P M g R S", "time": "Evening", "thaat": "Kafi", "mood": "Romantic, Spring"},
}

st.title("🎵 Raga Finder")
st.write("Type any Hindustani Raga name")

name = st.text_input("Raga Name", "Yaman")

if st.button("Get Details"):
    raga = RAGAS.get(name.strip().title())
    if raga:
        st.success(f"**{name.title()}**")
        st.write(f"**Thaat:** {raga['thaat']}")
        st.write(f"**Time:** {raga['time']}")
        st.write(f"**Aaroh:** {raga['aaroh']}")
        st.write(f"**Avroh:** {raga['avroh']}")
        st.write(f"**Mood:** {raga['mood']}")
    else:
        st.warning(f"{name} not in database. Try: Yaman, Bhairav, Malkauns, Bhairavi, Kafi")
