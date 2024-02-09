import streamlit as st
from openai import OpenAI
from prompts import *
import os

st.title('OpenAI GPT-3 Playground')
st.info('This is a simple playground to test OpenAI GPT-3 API. You can test the API by entering a prompt and see the response from the API.')


client = OpenAI()

def generate_revised_prompt(user_prompt, method):
    # This function is a placeholder for the actual logic you'd use to revise the prompt
    # based on the selected method. You might integrate with GPT here to generate
    # the revised prompt.
    # revised_prompt = generator(f"{method}: {user_prompt}", max_length=50)[0]['generated_text']
    # return revised_prompt
    pass

prompt_engineering_strategies = [
    "Generic Expert",
    "Imperfect Prompting",
    "Persistent Context and Custom Instructions Prompting",
    "Multi-Persona Prompting",
    "Chain-of-Thought (CoT) Prompting",
    "Retrieval-Augmented Generation (RAG) Prompting",
    "Chain-of-Thought Factored Decomposition Prompting",
    "Skeleton-of-Thought (SoT) Prompting",
    "Show-Me Versus Tell-Me Prompting",
    "Mega-Personas Prompting",
    "Certainty and Uncertainty Prompting",
    "Vagueness Prompting",
    "Catalogs or Frameworks for Prompting",
    "Flipped Interaction Prompting",
    "Self-Reflection Prompting",
    "Add-On Prompting",
    "Conversational Prompting",
    "Prompt-to-Code Prompting",
    "Target-Your-Response (TAYOR) Prompting",
    "Macros and End-Goal Prompting",
    "Tree-of-Thoughts (ToT) Prompting",
    "Trust Layers for Prompting",
    "Directional Stimulus Prompting (DSP)",
    "Privacy Invasive Prompting",
    "Illicit or Disallowed Prompting",
    "Chain-of-Density (CoD) Prompting",
    "Take a Deep Breath Prompting",
    "Chain-of-Verification (CoV) Prompting",
    "Beat the Reverse Curse Prompting",
    "Overcoming Dumbing Down Prompting",
    "DeepFakes to TrueFakes Prompting",
    "Disinformation Detection and Removal Prompting",
    "Emotionally Expressed Prompting"
]
method_mapping = {
    "Imperfect Prompting": system_prompt_Imperfect_Prompting,
    "Persistent Context and Custom Instructions Prompting": system_prompt_Persistent_Context_and_Custom_Instructions_Prompting,
    "Multi-Persona Prompting": system_prompt_Multi_Persona_Prompting,
    "Chain-of-Thought (CoT) Prompting": system_prompt_Chain_of_Thought_CoT_Prompting,
    "Retrieval-Augmented Generation (RAG) Prompting": system_prompt_Retrieval_Augmented_Generation_RAG_Prompting,
    "Chain-of-Thought Factored Decomposition Prompting": system_prompt_Chain_of_Thought_Factored_Decomposition_Prompting,
    "Skeleton-of-Thought (SoT) Prompting": system_prompt_Skeleton_of_Thought_SoT_Prompting,
    "Show-Me Versus Tell-Me Prompting": system_prompt_Show_Me_Versus_Tell_Me_Prompting,
    "Mega-Personas Prompting": system_prompt_Mega_Personas_Prompting,
    "Certainty and Uncertainty Prompting": system_prompt_Certainty_and_Uncertainty_Prompting,
    "Vagueness Prompting": system_prompt_Vagueness_Prompting,
    "Catalogs or Frameworks for Prompting": system_prompt_Catalogs_or_Frameworks_for_Prompting,
    "Flipped Interaction Prompting": system_prompt_Flipped_Interaction_Prompting,
    "Self-Reflection Prompting": system_prompt_Self_Reflection_Prompting,
    "Add-On Prompting": system_prompt_Add_On_Prompting,
    "Conversational Prompting": system_prompt_Conversational_Prompting,
    "Prompt-to-Code Prompting": system_prompt_Prompt_to_Code_Prompting,
    "Target-Your-Response (TAYOR) Prompting": system_prompt_Target_Your_Response_TAYOR_Prompting,
    "Macros and End-Goal Prompting": system_prompt_Macros_and_End_Goal_Prompting,
    "Tree-of-Thoughts (ToT) Prompting": system_prompt_Tree_of_Thoughts_ToT_Prompting,
    "Trust Layers for Prompting": system_prompt_Trust_Layers_for_Prompting,
    "Directional Stimulus Prompting (DSP)": system_prompt_Directional_Stimulus_Prompting_DSP,
    "Privacy Invasive Prompting": system_prompt_Privacy_Invasive_Prompting,
    "Illicit or Disallowed Prompting": system_prompt_Illicit_or_Disallowed_Prompting,
    "Chain-of-Density (CoD) Prompting": system_prompt_Chain_of_Density_CoD_Prompting,
    "Take a Deep Breath Prompting": system_prompt_Take_a_Deep_Breath_Prompting,
    "Chain-of-Verification (CoV) Prompting": system_prompt_Chain_of_Verification_CoV_Prompting,
    "Beat the Reverse Curse Prompting": system_prompt_Beat_the_Reverse_Curse_Prompting,
    "Overcoming Dumbing Down Prompting": system_prompt_Overcoming_Dumbing_Down_Prompting,
    "DeepFakes to TrueFakes Prompting": system_prompt_DeepFakes_to_TrueFakes_Prompting,
    "Disinformation Detection and Removal Prompting": system_prompt_Disinformation_Detection_and_Removal_Prompting,
    "Emotionally Expressed Prompting": system_prompt_Emotionally_Expressed_Prompting,
    "Generic Expert": system_prompt_Generic_Expert_Prompting
}

user_prompt = st.text_area("Enter your prompt:", height=150)

selected_strategies = st.multiselect(
    "Select one or more prompt engineering strategies:",
    options=prompt_engineering_strategies,
    default=None
)

with st.sidebar:
    for strategy in selected_strategies:
        strategy_string = method_mapping.get(strategy, "Unknown Strategy")
        st.write(f"Selected: {strategy_string}")

if st.button("Generate Response"):
    # Use the method_mapping to convert selected strategies to their string conventions
    revised_prompt = user_prompt
    for strategy in selected_strategies:
        strategy_string = method_mapping.get(strategy, "Unknown Strategy")
        revised_prompt = f"{strategy_string}: {revised_prompt}"
    
    # Send the revised prompt to your GPT model and get a response
    response = generate_response(revised_prompt)
    st.write(response)