# CreateMyRunJS

CreateMyRunJS is a web application that allows users to generate unique running routes based on their preferences. The application uses Google Maps API to display maps and calculate routes, and Azure Functions to handle server-side operations and logging.

Map can be tested on **https://createmyrun.com**

API Keys are restricted or deleted. Use your own.

## Features

- Generate running routes based on distance and starting location
- Display routes on Google Maps
- Log user interactions and feedback
- Store logs in Azure Blob Storage
- Send notifications to a Telegram chat

## Setup

### Prerequisites

- Node.js and npm installed
- Python 3.x installed
- Azure account with Blob Storage
- Google Maps API key
- Telegram Bot API token and chat ID

### Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/CreateMyRunJS.git
   cd CreateMyRunJS
   ```

2. Install dependencies:

   ```sh
   npm install
   ```

3. Set up environment variables:

   Create a `.env` file in the project root and add the following variables:

   ```env
   AZURE_STORAGE_CONNECTION_STRING=your_azure_storage_connection_string
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token
   TELEGRAM_CHAT_ID=your_telegram_chat_id
   ```

4. Deploy the Azure Function:

   Follow the [Azure Functions deployment guide](https://docs.microsoft.com/en-us/azure/azure-functions/functions-develop-vs-code) to deploy the function in `project/function_app.py`.

## Usage

1. Start the web server:

   ```sh
   npm start
   ```

2. Open your browser and navigate to `http://localhost:3000`.

3. Enter the desired distance and click on the map to choose your starting location.

4. Click "Create!" to generate the running route.

5. View the generated routes and click on the links to open them in Google Maps.

6. Provide feedback using the feedback form at the bottom of the page.

## Logging

Logs are managed by the `LogManager` class in `website/polyRun.js`. Logs are sent to an Azure Function endpoint and stored in Azure Blob Storage. Notifications are also sent to a Telegram chat.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
