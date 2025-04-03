import json
import argparse

def convert_to_chat_format(input_file, output_file):
    # Hard-coded system prompt
    system_prompt = "Your role as an assistant involves thoroughly exploring questions through a systematic long thinking process before providing the final precise and accurate solutions. This requires engaging in a comprehensive cycle of analysis, summarizing, exploration, reassessment, reflection, backtracing, and iteration to develop well-considered thinking process. Please structure your response into two main sections: Thought and Solution. In the Thought section, detail your reasoning process using the specified format: <think> {thought with steps separated with '\n\n'} <\/think> Each step should include detailed considerations such as analisying questions, summarizing relevant findings, brainstorming new ideas, verifying the accuracy of the current steps, refining any errors, and revisiting previous steps. In the Solution section, based on various attempts, explorations, and reflections from the Thought section, systematically present the final solution that you deem correct. The solution should remain a logical, accurate, concise expression style and detail necessary step needed to reach the conclusion, formatted as follows: <answer> {final formatted, precise, and clear solution} <\/answer> Now, try to solve the following question through the above guidelines:"
    
    # Read input file and convert each line
    with open(input_file, 'r', encoding='utf-8') as f_in:
        with open(output_file, 'w', encoding='utf-8') as f_out:
            for line in f_in:
                # Parse the original JSON
                data = json.loads(line.strip())
                
                # Extract the prompt
                prompt_text = data['prompt']
                
                # Create messages format
                messages = [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt_text}
                ]
                
                # Create new data structure
                new_data = {
                    "prompt": messages,
                    "answer": data['answer']
                }
                
                # Write to output file
                f_out.write(json.dumps(new_data, ensure_ascii=False) + '\n')
    
    print(f"Conversion complete. Output saved to {output_file}")

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Convert text prompts to chat format")
    parser.add_argument("input_file", type=str, help="Input JSONL file path")
    parser.add_argument("output_file", type=str, help="Output JSONL file path")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Run conversion
    convert_to_chat_format(args.input_file, args.output_file)

if __name__ == "__main__":
    main() 