(TeX-add-style-hook
 "deptlettertemplate2019"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "12pt")))
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art12"
    "epsfig"
    "longfbox"
    "fullpage"
    "url"
    "datetime"
    "lipsum"
    "fancyhdr"
    "fontspec"
    "xcolor"))
 :latex)

