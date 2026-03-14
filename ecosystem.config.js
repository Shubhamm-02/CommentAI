module.exports = {
  apps : [
    {
      name: "commentai-agent",
      script: "src/main.py",
      interpreter: "python3",
      watch: false,
      env: { "NODE_ENV": "production" }
    },
    {
      name: "commentai-dashboard",
      script: "src/api_server.py",
      interpreter: "python3",
      watch: false,
      env: { "NODE_ENV": "production" }
    }
  ]
}
