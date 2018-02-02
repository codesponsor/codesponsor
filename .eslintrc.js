const error = 2;
const warn = 1;
const ignore = 0;

module.exports = {
  extends: ['prettier'],
  plugins: ['prettier'],
  env: {
    es6: true,
    node: true,
  },
  parser: 'babel-eslint',
  parserOptions: {
    sourceType: 'module',
  },
  rules: {
    'no-console': ['error', { allow: ['warn', 'error'] }],
    'no-labels': warn,
    'no-cond-assign': error,
    'no-constant-condition': error,
    'no-control-regex': error,
    'no-debugger': error,
    'no-dupe-args': error,
    'no-dupe-keys': error,
    'no-duplicate-case': error,
    'no-empty': ['error', { allowEmptyCatch: true }],
    'no-empty-character-class': error,
    'no-ex-assign': error,
    'no-extra-boolean-cast': error,
    'no-extra-semi': error,
    'no-func-assign': error,
    'no-inner-declarations': [2, 'functions'],
    'no-invalid-regexp': error,
    'no-irregular-whitespace': error,
    'no-negated-in-lhs': error,
    'no-obj-calls': error,
    'no-regex-spaces': error,
    'no-sparse-arrays': error,
    'no-unexpected-multiline': error,
    'no-unreachable': error,
    'use-isnan': error,
    'valid-typeof': error,
    'accessor-pairs': error,
    eqeqeq: error,
    'guard-for-in': error,
    'no-alert': error,
    'no-caller': error,
    'no-case-declarations': error,
    'no-div-regex': error,
    'no-labels': error,
    'no-empty-pattern': error,
    'no-eq-null': error,
    'no-eval': error,
    'no-extend-native': error,
    'no-extra-bind': error,
    'no-fallthrough': error,
    'no-implied-eval': error,
    'no-iterator': error,
    'no-lone-blocks': error,
    'no-loop-func': error,
    'no-native-reassign': error,
    'no-new-func': error,
    'no-new-wrappers': error,
    'no-new': error,
    'no-octal-escape': error,
    'no-octal': error,
    'no-proto': error,
    'no-redeclare': error,
    'no-return-assign': error,
    'no-script-url': error,
    'no-self-compare': error,
    'no-unused-expressions': error,
    'no-useless-call': error,
    'no-useless-concat': error,
    'no-void': error,
    'no-with': error,
    radix: error,
    'wrap-iife': error,
    'no-catch-shadow': error,
    'no-delete-var': error,
    'no-label-var': error,
    'no-shadow-restricted-names': error,
    'no-undef-init': error,
    'no-unused-vars': [
      'error',
      { argsIgnorePattern: '^_', ignoreRestSiblings: true },
    ],
    'global-require': error,
    'handle-callback-err': error,
    'no-path-concat': error,
    'no-process-exit': error,
    'max-statements': [2, 60],
  },
};
