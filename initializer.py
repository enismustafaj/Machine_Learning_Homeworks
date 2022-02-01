import jinja2
import os
import shutil


def generate_stubs(number_of_stubs, root_directory='.'):
    tm_loader = jinja2.FileSystemLoader(searchpath='./')
    tm_env = jinja2.Environment(
        block_start_string='\BLOCK{',
        block_end_string='}',
        variable_start_string='\VAR{',
        variable_end_string='}',
        comment_start_string='\#{',
        comment_end_string='}',
        line_statement_prefix='%%',
        line_comment_prefix='%#',
        trim_blocks=True,
        autoescape=False,
        loader=tm_loader
    )
    tm_file = 'template.tex'
    tm = tm_env.get_template(tm_file)

    for i in range(1, number_of_stubs + 1):
        homework_directory = f'{root_directory}/hw{i:02d}'

        if os.path.exists(homework_directory):
            shutil.rmtree(homework_directory)

        os.makedirs(homework_directory)
        os.chdir(homework_directory)

        with open(f'hw{i:02d}.tex', 'w+') as f:
            data = {
                'number': str(i)
            }
            f.write(tm.render(data))

        os.chdir('../')


if __name__ == '__main__':
    number_of_stubs = 10

    generate_stubs(number_of_stubs)
