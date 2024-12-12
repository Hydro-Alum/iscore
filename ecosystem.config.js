module.exports = {
    apps: [
        {
            name: 'iscore',
            script: '../venv/bin/gunicorn',
            args: '-c gunicorn_config.py run:app',
            instances: 1,
            exec_mode: 'fork',
            autorestart: true,
            max_restarts: 5,
            watch: false,
            max_memory_restart: '300M',
            env: {
                ENVIRONMENT: 'production',
            },
            error_file: '../logs/pm2-error.log',
            out_file: '../logs/pm2-output.log',
            log_date_format: 'YYYY-MM-DD HH:mm:ss Z',
        },
    ],
};