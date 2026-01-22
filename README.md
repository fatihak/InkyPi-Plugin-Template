# InkyPi-Plugin-Template
Use this template for creating new MagicMirror² modules.

See the [wiki page](https://github.com/fatihak/InkyPi/wiki) for an in depth overview of how to get started.

# InkyPi-Plugin-Template

*InkyPi-Template* is a plugin for [InkyPi](https://github.com/fatihak/InkyPi) that displays ... [Module description]

## Screenshot

![Example of InkyPi-Plugin-Template](./example.png)

## Installation

### Install

In your terminal, navigate to the plugin directory and clone the repository:

```bash
cd ~/InkyPi/src/modules
git clone [GitHub url]
```

Install additional dependencies: (if any are required)
```bash
cd ~/InkyPi/src/modules/InkyPi-Template
source "/usr/local/inkypi/venv_inkypi/bin/activate"
pip install -r requirements.txt
deactivate
```

### Update

Go to the module directory and pull the latest changes:

```bash
cd ~/InkyPi/src/modules/InkyPi-Template
git pull
```

## API Keys

- Login in to your account ... []
...
- Store your api key in the .env file with the key `SAMPLE_KEY`
    ```
    SAMPLE_KEY=your-key
    ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.