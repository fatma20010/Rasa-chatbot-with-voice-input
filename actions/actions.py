from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionHandleFAQ(Action):
    def name(self) -> Text:
        return "action_handle_faq"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        intent = tracker.latest_message['intent']['name']
        
        faqs = {
            # General inquiries
            "greet": "Hello! I'm your AI assistant. How can I help you today?",
            "goodbye": "Goodbye! Feel free to come back if you have more questions.",
            "thanks": "You're welcome! Is there anything else I can help you with?",
            
            # Product information
            "ask_product_info": "Our AI solution offers:\n- Advanced machine learning capabilities\n- Real-time data processing\n- Custom automation tools\n- Integration with existing systems\nWhich aspect would you like to know more about?",
            "ask_product_features": "Our key features include:\n- Natural language processing\n- Predictive analytics\n- Automated reporting\n- Custom workflows\n- 24/7 operation\nWould you like details about any specific feature?",
            "ask_product_demo": "I'd be happy to arrange a demo! You can schedule one at demo@example.com or call our sales team at 1-800-DEMO.",
            
            # Pricing and plans
            "ask_pricing": "We offer several pricing tiers:\n- Basic: $49/month\n- Professional: $99/month\n- Enterprise: Custom pricing\nWould you like to know what's included in each plan?",
            "ask_payment_methods": "We accept:\n- Credit/Debit cards\n- PayPal\n- Bank transfers\n- Purchase orders (Enterprise only)",
            "ask_refund_policy": "We offer a 30-day money-back guarantee on all plans. Would you like to know more about our refund process?",
            
            # Technical support
            "ask_support": "Our support options include:\n- 24/7 live chat\n- Email support\n- Phone support\n- Knowledge base\nHow would you prefer to get help?",
            "ask_technical_issue": "I can help with common technical issues. Could you describe the problem you're experiencing?",
            "ask_maintenance": "We perform maintenance every Sunday 2-4 AM EST. Emergency maintenance is announced 24 hours in advance.",
            
            # Account management
            "ask_account_setup": "Setting up an account is easy! Would you like me to guide you through the process?",
            "ask_password_reset": "You can reset your password through the 'Forgot Password' link on the login page, or I can help you do it now.",
            "ask_account_deletion": "To delete your account, please contact our support team. Would you like the contact information?",
            
            # Training and resources
            "ask_training": "We offer:\n- Video tutorials\n- Live webinars\n- Documentation\n- Custom training sessions\nWhat type of training interests you?",
            "ask_documentation": "Our documentation is available at docs.example.com. Would you like me to point you to a specific section?",
            
            # Security and compliance
            "ask_security": "We maintain high security standards with:\n- End-to-end encryption\n- Regular security audits\n- GDPR compliance\n- SOC 2 certification\nWould you like details about any specific security measure?",
            "ask_data_privacy": "We take data privacy seriously. All data is encrypted and stored in compliance with GDPR and CCPA. Would you like our full privacy policy?",
            
            # Integration and compatibility
            "ask_integration": "We integrate with:\n- CRM systems\n- Marketing platforms\n- Analytics tools\n- Custom APIs\nWhich integration are you interested in?",
            "ask_system_requirements": "Our system requires:\n- Modern web browser\n- Internet connection\n- 2GB RAM minimum\nDo you need specific compatibility information?",
            
            # Contact and company info
            "ask_contact": "You can reach us through:\n- Email: support@example.com\n- Phone: 1-800-AI-HELP\n- Office: 123 Tech Street, Innovation City",
            "ask_company_info": "We're a leading AI company founded in 2020, with offices worldwide. Would you like to know more about our company?",
            
            # Default response
            "default": "I'm not sure I understand. Could you rephrase that? You can ask about our products, pricing, support, or company information."
        }
        
        response = faqs.get(intent, faqs["default"])
        dispatcher.utter_message(text=response)
        return []