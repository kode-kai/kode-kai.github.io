# kode-kai.github.io

## Development  

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

To view the website, use `pelican content && pelican --listen` inside the environment.

Considerations:  

 - If modifying the theme's css, remember to minify the file with: `python -m csscompressor clean-blog/static/css/clean-blog.css > clean-blog/static/css/clean-blog.min.css`