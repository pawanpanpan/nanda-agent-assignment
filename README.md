# nanda-agent-assignment
NANDA Agent deployment for homework assignment

# NANDA Agent Assignment

## Agent Details
- **Agent ID**: agents461119
- **Domain**: sabaifire.com
- **Public URL**: http://3.144.161.206:6000
- **Status**: Successfully deployed and running

## What This Agent Does
This agent mimic myself as an MBA student and finance enthusiasm

## Deployment Steps
1. Launched EC2 instance with security groups configured
2. Configured DNS A record for sabaifire.com → 3.144.161.206
3. Generated SSL certificates using certbot
4. Installed Python 3.11 and NANDA adapter
5. Deployed agent with custom improvement logic

## API Endpoints
- GET https://sabaifire.com:6001/api/health - Health check
- POST https://sabaifire.com:6001/api/send - Send message to agent
- GET https://sabaifire.com:6001/api/agents/list - List registered agents

## Assignment Evidence
- Agent successfully started with ID: agents461119
- SSL certificates configured for production deployment
- Agent discoverable at: https://chat.nanda-registry.com/landing.html?agentId=agents461119
- Both A2A and HTTPS endpoints operational

## Feedback on NANDA Adapter
**Positive aspects:**
- Easy installation with pip
- Good documentation and examples
- Automatic SSL certificate integration
- Built-in agent registration and discovery
- Supports multiple AI frameworks

**Challenges encountered:**
- Registry connection timeouts
- Need for proper domain and SSL setup for full functionality
