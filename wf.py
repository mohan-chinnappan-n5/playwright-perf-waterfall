import streamlit as st
import plotly.graph_objects as go
import json
import textwrap

# Function to wrap text into multiple lines
def wrap_text(text, width):
    return "<br>".join(textwrap.wrap(text, width))

# Function to draw the waterfall chart
def draw_waterfall_chart(perf_data):
    resources = perf_data["resources"]
    
    # Prepare data for plotting
    fig = go.Figure()

    for resource in resources:
        folded_name = wrap_text(resource["name"], 60)  # Wrap text to 60 chars per line
        fig.add_trace(go.Scatter(
            x=[resource["startTime"], resource["startTime"] + resource["duration"]],
            y=[folded_name, folded_name],
            mode='lines',
            line=dict(color='royalblue', width=12)  # Increased line width for thicker bars
        ))

    fig.update_layout(
        title="Waterfall Chart",
        xaxis_title="Time (ms)",
        yaxis_title="Resource",
        showlegend=False,
        yaxis=dict(autorange="reversed", showgrid=True),  # Combine yaxis options here
        xaxis=dict(showgrid=True)
    )

    return fig

# Streamlit App
def main():
    st.title("Waterfall Chart Visualization (for Playwright)")

    # Upload JSON file
    uploaded_file = st.file_uploader("Choose a JSON file", type="json")
    
    if uploaded_file is not None:
        # Read the JSON file
        perf_data = json.load(uploaded_file)
        
        # Option to show the JSON file contents
        if st.checkbox("Show JSON file contents"):
            st.subheader("JSON File Contents")
            st.json(perf_data)

        # Draw the waterfall chart
        fig = draw_waterfall_chart(perf_data)
        st.plotly_chart(fig)

if __name__ == "__main__":
    main()
