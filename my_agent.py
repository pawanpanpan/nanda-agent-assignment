#!/usr/bin/env python3
from nanda_adapter import NANDA
import os

def create_custom_improvement():
    """Create your custom improvement function"""
    
    def custom_improvement_logic(message_text: str) -> str:
        """Transform messages according to your logic"""
        try:
            # Simple example: make text more polite and add flair
            improved_text = message_text.replace("hey", "hello")
            improved_text = improved_text.replace("yeah", "yes")
            
            return f"[IMPROVED]: {improved_text}"
        except Exception as e:
            print(f"Error in improvement: {e}")
            return message_text  # Fallback to original
    
    return custom_improvement_logic

def main():
    print("Starting NANDA Agent...")
    
    # Get environment variables
    anthropic_key = os.getenv("ANTHROPIC_API_KEY")
    domain = os.getenv("DOMAIN_NAME")
    
    if not anthropic_key:
        print("ERROR: ANTHROPIC_API_KEY not set!")
        print("Please set your API key first.")
        input("Press Enter to exit...")
        return
        
    if not domain:
        print("ERROR: DOMAIN_NAME not set!")
        print("Please set your domain name first.")
        input("Press Enter to exit...")
        return
    
    print(f"Using domain: {domain}")
    print("Creating improvement function...")
    
    # Create your improvement function
    my_improvement = create_custom_improvement()
    
    # Initialize NANDA with your custom logic
    print("Initializing NANDA...")
    nanda = NANDA(my_improvement)
    
    # Start the server
    print("Starting server...")
    nanda.start_server_api(anthropic_key, domain)

if __name__ == "__main__":
    main()