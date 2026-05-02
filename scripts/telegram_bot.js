const { Telegraf } = require('telegraf');
const { exec } = require('child_process');
const path = require('path');
require('dotenv').config({ path: path.join(__dirname, '..', '.env') });

const bot = new Telegraf(process.env.TELEGRAM_TOKEN);

// مسار run_skill.py
const RUNNER = path.join(__dirname, 'run_skill.py');

function runSkill(skillName, args, callback) {
    const argsJson = JSON.stringify(args).replace(/"/g, '\\"');
    const cmd = `python "${RUNNER}" ${skillName} "${argsJson}"`;
    
    exec(cmd, { cwd: path.join(__dirname, '..') }, (error, stdout, stderr) => {
        if (error) {
            console.error('Exec error:', error);
            return callback(error);
        }
        try {
            const result = JSON.parse(stdout.trim());
            callback(null, result);
        } catch (e) {
            callback(new Error('Invalid output: ' + stdout.substring(0, 200)));
        }
    });
}

// /start
bot.command('start', (ctx) => {
    ctx.reply(
        `🤖 *Data Analyst Agent*\n\n` +
        `*Commands:*\n` +
        `/analyze — Full dataset analysis\n` +
        `/plot — Price & Volume chart\n` +
        `/ask [question] — Ask about the data\n\n` +
        `Example: /ask what is the highest price?`,
        { parse_mode: 'Markdown' }
    );
});

// /analyze
bot.command('analyze', (ctx) => {
    ctx.reply('⏳ Analyzing data...');
    runSkill('analyze', {}, (err, result) => {
        if (err || result.status !== 'success') {
            return ctx.reply('❌ Error: ' + (err?.message || result?.message));
        }
        ctx.reply(result.summary, { parse_mode: 'Markdown' });
    });
});

// /plot
bot.command('plot', (ctx) => {
    ctx.reply('⏳ Generating chart...');
    runSkill('plot', { chart_type: 'price_history', x_column: 'Date', y_column: 'Close' }, (err, result) => {
        if (err || result.status !== 'success') {
            return ctx.reply('❌ Error: ' + (err?.message || result?.message));
        }
        ctx.replyWithPhoto(
            { source: result.image_path },
            { caption: '📊 Saudi Aramco (2222.SR) — Price & Volume' }
        );
    });
});

// /ask
bot.command('ask', (ctx) => {
    const question = ctx.message.text.replace('/ask', '').trim();
    if (!question) {
        return ctx.reply('❓ Please add a question.\nExample: /ask what is the highest price?');
    }
    
    ctx.reply('⏳ Thinking...');
    runSkill('ask', { question: question }, (err, result) => {
        if (err || result.status !== 'success') {
            return ctx.reply('❌ Error: ' + (err?.message || result?.message));
        }
        ctx.reply(result.answer, { parse_mode: 'Markdown' });
    });
});

// تشغيل البوت
bot.launch();
console.log('🤖 Bot is running... Press Ctrl+C to stop.');

// إيقاف نظيف
process.once('SIGINT', () => bot.stop('SIGINT'));
process.once('SIGTERM', () => bot.stop('SIGTERM'));