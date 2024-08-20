from crewai import Crew,Process
from agents import blog_researcher,blog_writer
from tasks import research_task,write_task


# Forming the tech-focused crew with some enhanced configurations
crew = Crew(
  agents=[blog_researcher, blog_writer],
  tasks=[research_task, write_task],
  process=Process.sequential,  # Optional: Sequential task execution is default
  memory=True,
  cache=True,
  max_rpm=100,
  share_crew=True
)

## start the task execution process with enhanced feedback
result=crew.kickoff(inputs={'topic':'AI VS ML VS DL vs Data Science'})
print(result)

#ui try

# import streamlit as st
# from crewai import Crew, Process
# from agents import blog_researcher, blog_writer
# from tasks import research_task, write_task

# # Initialize the Crew instance
# crew = Crew(
#     agents=[blog_researcher, blog_writer],
#     tasks=[research_task, write_task],
#     process=Process.sequential,  # Sequential task execution is default
#     memory=True,
#     cache=True,
#     max_rpm=100,
#     share_crew=True
# )

# # Streamlit UI
# st.title("AI Blog Content Creator")

# # Input for topic
# topic = st.text_input("Enter the topic for the blog:", "AI VS ML VS DL vs Data Science")

# # Button to start the process
# if st.button("Kickoff Task Execution"):
#     # Start the task execution process
#     with st.spinner("Executing tasks..."):
#         result = crew.kickoff(inputs={'topic': topic})
    
#     # Display the result
#     st.success("Task Execution Completed!")
#     st.write("**Result:**")
#     st.write(result)

# # Footer
# st.write("Powered by CrewAI")
