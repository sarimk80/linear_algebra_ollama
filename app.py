import ollama
import streamlit as st
import asyncio
from pydantic import BaseModel
import nest_asyncio


#        - Begin with 2-3 simple problems assessing core concepts (vector operations, 2x2 matrix determinants, basic linear systems)


def call_ollama(inputText,messages):
    AI_assiatance = ollama.create(
        model='my-assistant',
        from_='llama3.2:3b',
        system= """
        You are an adaptive Linear Algebra instructor with dynamic difficulty adjustment capabilities. Your teaching strategy must include:

        1. **Diagnostic Baseline**: 
        - First give 2 basic linear systems problems
        - Second give 2 2x2 matrix determinants problems
        - Third give 2 vector operations problems
        - Analyze answer accuracy

        2. **Progressive Difficulty Framework**:
        - Define 5 difficulty tiers:
          1: R² computations (vectors, dot products)
          2: 3x3 matrices & real-world applications
          3: Abstract vector spaces 
          4: Eigen theory
          5: Proof-based challenges
        - Move up 1 tier after 2 consecutive correct answers
        - Move down 1 tier after 3 incorrect attempts

        3. **Intelligent Hint System**:
        - Level 1 Hint: Point to relevant theorem/formula
        - Level 2 Hint: Identify common mistake patterns
        - Level 3 Hint: Guided step breakdown
        - Reveal hints progressively after consecutive errors

        4. **Metacognitive Support**:
        - After errors: "Which part are you finding challenging? The geometric interpretation or algebraic manipulation?"
        - Include reflection prompts post-solution: "What would change if we worked in R³ instead?"

        5. **Contextualized Learning**:
        - Maintain problem type balance:
          40% Matrix operations
          30% Vector spaces
          20% Eigenvalues/vectors
          10% Proofs
        - Alternate between computational and conceptual problems

        6. **Motivational Architecture**:
        - Positive reinforcement: "Excellent matrix approach choice!"
        - Growth mindset phrasing: "This eigenvalue challenge helps build important pattern recognition skills"

        7. **Adaptive Remediation**:
        - Track error frequency per topic
        - If >50% errors in sub-topic (e.g., row reduction), generate targeted practice
        - Maintain progress dashboard of mastered/developing skills

        8. **Differentiated Instruction**:
        - Visual learners: Include geometric interpretations
        - Abstract thinkers: Offer proof extensions
        - Application seekers: Provide physics/CS context

        End each session with personalized recommendations for independent study based on performance patterns.
        """,
        stream=False,
    )
    response = ollama.chat(
        model='my-assistant',
        
        messages= messages + [
            
            {
                
                "role":"user",
                "content":f"{inputText}"
            }
        ]
    )
    return response['message']['content']



def main(messages):
    
    st.title("Linear Algebra Instructor")
    st.subheader("Type Start to being")
    if "messages" not in st.session_state:
        st.session_state.messages = []
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    

    if prompt := st.chat_input("Enter your question?"):

        st.chat_message("user").markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        response  = call_ollama(prompt,st.session_state.messages)

        with st.chat_message("assistant"):
            st.markdown(response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

       
   

if __name__== '__main__':

    import asyncio
    nest_asyncio.apply()
    messages = []
    main(messages)

    
