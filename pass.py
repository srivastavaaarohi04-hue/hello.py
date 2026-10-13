```python
import streamlit as st
import re

# Page configuration
st.set_page_config(
    page_title="Password Strength Checker",
    page_icon="🔐",
    layout="centered"
)

# Heading
st.title("🔐 Password Strength Checker")
st.write("Enter a sample password to check its strength.")
st.info("⚠️ Do not enter your actual personal password. Use a test password.")

# Password input
password = st.text_input(
    "Enter Password:",
    type="password",
    placeholder="Enter a sample password"
)

if password:
    # Check password criteria
    length_check = len(password) >= 8
    uppercase_check = bool(re.search(r"[A-Z]", password))
    lowercase_check = bool(re.search(r"[a-z]", password))
    number_check = bool(re.search(r"[0-9]", password))
    special_check = bool(re.search(r"[^A-Za-z0-9]", password))

    # Calculate score
    score = sum([
        length_check,
        uppercase_check,
        lowercase_check,
        number_check,
        special_check
    ])

    # Determine strength
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    # Display strength
    st.subheader("Password Strength Analysis")

    if strength == "Weak":
        st.error(f"🔴 Strength: {strength}")
    elif strength == "Moderate":
        st.warning(f"🟡 Strength: {strength}")
    else:
        st.success(f"🟢 Strength: {strength}")

    # Score
    st.write(f"### Password Strength Score: {score}/5")
    st.progress(score / 5)

    # Checklist
    st.subheader("✅ Criteria Checklist")

    if length_check:
        st.success("✔ At least 8 characters")
    else:
        st.error("✘ At least 8 characters")

    if uppercase_check:
        st.success("✔ Contains an uppercase letter")
    else:
        st.error("✘ Contains an uppercase letter")

    if lowercase_check:
        st.success("✔ Contains a lowercase letter")
    else:
        st.error("✘ Contains a lowercase letter")

    if number_check:
        st.success("✔ Contains a number")
    else:
        st.error("✘ Contains a number")

    if special_check:
        st.success("✔ Contains a special character")
    else:
        st.error("✘ Contains a special character")

    # Suggestions
    if score < 5:
        st.subheader("💡 Suggestions for Improvement")

        if not length_check:
            st.write("• Use at least 8 characters.")

        if not uppercase_check:
            st.write("• Add at least one uppercase letter (A-Z).")

        if not lowercase_check:
            st.write("• Add at least one lowercase letter (a-z).")

        if not number_check:
            st.write("• Add at least one number (0-9).")

        if not special_check:
            st.write("• Add at least one special character such as !, @, #, or $.")

    else:
        st.success("🎉 Excellent! Your sample password meets all five criteria.")
```
