(require 'lsp-mode)

(with-eval-after-load 'lsp-mode
  (add-to-list 'lsp-language-id-configuration
               '(dummy-mode . "dummylsp"))
  (lsp-register-client
   (make-lsp-client :new-connection (lsp-stdio-connection "dummylsp")
                    :activation-fn (lsp-activate-on "dummylsp")
                    :server-id 'dummylsp)))
