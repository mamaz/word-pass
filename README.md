# An XKCD style password generator with meaningful words

Based on XKCD [#936](https://xkcd.com/936/)

It's still work in progress

I plan to create more easy to remember words, right now it's still random.

## Usage

1. Clone this project

2. Install pip

3. Run `pip install -r requirements.txt`

4. At root project, run `python -m password` or add additional command to add language (id,end) and word length: `python -m password --language=id --length=4`

Requires python version >= 3.4

## Example


```
➜ python -m password
item arrest native should

➜ python -m password --language=id
bidang bus distingtif gondol

➜ python -m password --language=id --length=6
gundal alkohol abjad geragau fulus cespleng
```

## License

MIT
