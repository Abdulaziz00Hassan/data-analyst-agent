import sys
import json
import os
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
skill_name = sys.argv[1]
args_json = sys.argv[2] if len(sys.argv) > 2 else '{}'
args = json.loads(args_json)

# إضافة root للمسار
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# المسار الافتراضي للبيانات
default_data = os.path.join(os.path.dirname(__file__), '..', 'data', 'aramco_stock.csv')

if skill_name == 'analyze':
    from skills.analyze_csv.analyze import analyze_csv
    result = analyze_csv(args.get('file_path', default_data))
    
elif skill_name == 'plot':
    from skills.plot_chart.plot import plot_chart
    result = plot_chart(
        args.get('file_path', default_data),
        args.get('chart_type', 'line'),
        args.get('x_column', 'Date'),
        args.get('y_column', 'Close'),
        args.get('title')
    )
    
elif skill_name == 'ask':
    from skills.ask_data.ask import ask_data
    result = ask_data(
        args.get('file_path', default_data),
        args.get('question', '')
    )
    
else:
    result = {'status': 'error', 'message': f'Unknown skill: {skill_name}'}

print(json.dumps(result, indent=2, ensure_ascii=False))