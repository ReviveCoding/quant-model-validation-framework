# Local and GitHub Runnable Audit

Generated: 2026-06-04

## Required structure

| item                     | exists   | type   |
|:-------------------------|:---------|:-------|
| README.md                | True     | file   |
| PROJECT_CARD.md          | True     | file   |
| Makefile                 | True     | file   |
| pyproject.toml           | True     | file   |
| requirements.txt         | True     | file   |
| .gitignore               | True     | file   |
| Dockerfile               | True     | file   |
| .dockerignore            | True     | file   |
| .github/workflows/ci.yml | True     | file   |
| scripts/run_pipeline.py  | True     | file   |
| tests                    | True     | dir    |
| src                      | True     | dir    |
| configs                  | True     | dir    |
| outputs                  | True     | dir    |
| reports                  | True     | dir    |

## Non-GitHub artifacts detected

| non_github_artifact                                                           |
|:------------------------------------------------------------------------------|
| .pytest_cache                                                                 |
| .venv\Lib\site-packages\__pycache__                                           |
| .venv\Lib\site-packages\colorama\__pycache__                                  |
| .venv\Lib\site-packages\colorama\tests\__pycache__                            |
| .venv\Lib\site-packages\dateutil\__pycache__                                  |
| .venv\Lib\site-packages\dateutil\parser\__pycache__                           |
| .venv\Lib\site-packages\dateutil\tz\__pycache__                               |
| .venv\Lib\site-packages\dateutil\zoneinfo\__pycache__                         |
| .venv\Lib\site-packages\iniconfig\__pycache__                                 |
| .venv\Lib\site-packages\numpy\__pycache__                                     |
| .venv\Lib\site-packages\numpy\array_api\__pycache__                           |
| .venv\Lib\site-packages\numpy\array_api\tests\__pycache__                     |
| .venv\Lib\site-packages\numpy\compat\__pycache__                              |
| .venv\Lib\site-packages\numpy\compat\tests\__pycache__                        |
| .venv\Lib\site-packages\numpy\core\__pycache__                                |
| .venv\Lib\site-packages\numpy\core\tests\__pycache__                          |
| .venv\Lib\site-packages\numpy\core\tests\examples\cython\__pycache__          |
| .venv\Lib\site-packages\numpy\core\tests\examples\limited_api\__pycache__     |
| .venv\Lib\site-packages\numpy\distutils\__pycache__                           |
| .venv\Lib\site-packages\numpy\distutils\command\__pycache__                   |
| .venv\Lib\site-packages\numpy\distutils\fcompiler\__pycache__                 |
| .venv\Lib\site-packages\numpy\distutils\tests\__pycache__                     |
| .venv\Lib\site-packages\numpy\doc\__pycache__                                 |
| .venv\Lib\site-packages\numpy\f2py\__pycache__                                |
| .venv\Lib\site-packages\numpy\f2py\tests\__pycache__                          |
| .venv\Lib\site-packages\numpy\f2py\_backends\__pycache__                      |
| .venv\Lib\site-packages\numpy\fft\__pycache__                                 |
| .venv\Lib\site-packages\numpy\fft\tests\__pycache__                           |
| .venv\Lib\site-packages\numpy\lib\__pycache__                                 |
| .venv\Lib\site-packages\numpy\lib\tests\__pycache__                           |
| .venv\Lib\site-packages\numpy\linalg\__pycache__                              |
| .venv\Lib\site-packages\numpy\linalg\tests\__pycache__                        |
| .venv\Lib\site-packages\numpy\ma\__pycache__                                  |
| .venv\Lib\site-packages\numpy\ma\tests\__pycache__                            |
| .venv\Lib\site-packages\numpy\matrixlib\__pycache__                           |
| .venv\Lib\site-packages\numpy\matrixlib\tests\__pycache__                     |
| .venv\Lib\site-packages\numpy\polynomial\__pycache__                          |
| .venv\Lib\site-packages\numpy\polynomial\tests\__pycache__                    |
| .venv\Lib\site-packages\numpy\random\__pycache__                              |
| .venv\Lib\site-packages\numpy\random\tests\__pycache__                        |
| .venv\Lib\site-packages\numpy\random\tests\data\__pycache__                   |
| .venv\Lib\site-packages\numpy\random\_examples\cffi\__pycache__               |
| .venv\Lib\site-packages\numpy\random\_examples\numba\__pycache__              |
| .venv\Lib\site-packages\numpy\testing\__pycache__                             |
| .venv\Lib\site-packages\numpy\testing\tests\__pycache__                       |
| .venv\Lib\site-packages\numpy\testing\_private\__pycache__                    |
| .venv\Lib\site-packages\numpy\tests\__pycache__                               |
| .venv\Lib\site-packages\numpy\typing\__pycache__                              |
| .venv\Lib\site-packages\numpy\typing\tests\__pycache__                        |
| .venv\Lib\site-packages\numpy\typing\tests\data\pass\__pycache__              |
| .venv\Lib\site-packages\numpy\_core\__pycache__                               |
| .venv\Lib\site-packages\numpy\_pyinstaller\__pycache__                        |
| .venv\Lib\site-packages\numpy\_typing\__pycache__                             |
| .venv\Lib\site-packages\numpy\_utils\__pycache__                              |
| .venv\Lib\site-packages\packaging\__pycache__                                 |
| .venv\Lib\site-packages\packaging\licenses\__pycache__                        |
| .venv\Lib\site-packages\pandas\__pycache__                                    |
| .venv\Lib\site-packages\pandas\api\__pycache__                                |
| .venv\Lib\site-packages\pandas\api\extensions\__pycache__                     |
| .venv\Lib\site-packages\pandas\api\indexers\__pycache__                       |
| .venv\Lib\site-packages\pandas\api\interchange\__pycache__                    |
| .venv\Lib\site-packages\pandas\api\types\__pycache__                          |
| .venv\Lib\site-packages\pandas\api\typing\__pycache__                         |
| .venv\Lib\site-packages\pandas\arrays\__pycache__                             |
| .venv\Lib\site-packages\pandas\compat\__pycache__                             |
| .venv\Lib\site-packages\pandas\compat\numpy\__pycache__                       |
| .venv\Lib\site-packages\pandas\core\__pycache__                               |
| .venv\Lib\site-packages\pandas\core\arrays\__pycache__                        |
| .venv\Lib\site-packages\pandas\core\arrays\arrow\__pycache__                  |
| .venv\Lib\site-packages\pandas\core\arrays\sparse\__pycache__                 |
| .venv\Lib\site-packages\pandas\core\array_algos\__pycache__                   |
| .venv\Lib\site-packages\pandas\core\computation\__pycache__                   |
| .venv\Lib\site-packages\pandas\core\dtypes\__pycache__                        |
| .venv\Lib\site-packages\pandas\core\groupby\__pycache__                       |
| .venv\Lib\site-packages\pandas\core\indexers\__pycache__                      |
| .venv\Lib\site-packages\pandas\core\indexes\__pycache__                       |
| .venv\Lib\site-packages\pandas\core\interchange\__pycache__                   |
| .venv\Lib\site-packages\pandas\core\internals\__pycache__                     |
| .venv\Lib\site-packages\pandas\core\methods\__pycache__                       |
| .venv\Lib\site-packages\pandas\core\ops\__pycache__                           |
| .venv\Lib\site-packages\pandas\core\reshape\__pycache__                       |
| .venv\Lib\site-packages\pandas\core\sparse\__pycache__                        |
| .venv\Lib\site-packages\pandas\core\strings\__pycache__                       |
| .venv\Lib\site-packages\pandas\core\tools\__pycache__                         |
| .venv\Lib\site-packages\pandas\core\util\__pycache__                          |
| .venv\Lib\site-packages\pandas\core\window\__pycache__                        |
| .venv\Lib\site-packages\pandas\core\_numba\__pycache__                        |
| .venv\Lib\site-packages\pandas\core\_numba\kernels\__pycache__                |
| .venv\Lib\site-packages\pandas\errors\__pycache__                             |
| .venv\Lib\site-packages\pandas\io\__pycache__                                 |
| .venv\Lib\site-packages\pandas\io\clipboard\__pycache__                       |
| .venv\Lib\site-packages\pandas\io\excel\__pycache__                           |
| .venv\Lib\site-packages\pandas\io\formats\__pycache__                         |
| .venv\Lib\site-packages\pandas\io\json\__pycache__                            |
| .venv\Lib\site-packages\pandas\io\parsers\__pycache__                         |
| .venv\Lib\site-packages\pandas\io\sas\__pycache__                             |
| .venv\Lib\site-packages\pandas\plotting\__pycache__                           |
| .venv\Lib\site-packages\pandas\plotting\_matplotlib\__pycache__               |
| .venv\Lib\site-packages\pandas\tests\__pycache__                              |
| .venv\Lib\site-packages\pandas\tests\api\__pycache__                          |
| .venv\Lib\site-packages\pandas\tests\apply\__pycache__                        |
| .venv\Lib\site-packages\pandas\tests\arithmetic\__pycache__                   |
| .venv\Lib\site-packages\pandas\tests\arrays\__pycache__                       |
| .venv\Lib\site-packages\pandas\tests\arrays\boolean\__pycache__               |
| .venv\Lib\site-packages\pandas\tests\arrays\categorical\__pycache__           |
| .venv\Lib\site-packages\pandas\tests\arrays\datetimes\__pycache__             |
| .venv\Lib\site-packages\pandas\tests\arrays\floating\__pycache__              |
| .venv\Lib\site-packages\pandas\tests\arrays\integer\__pycache__               |
| .venv\Lib\site-packages\pandas\tests\arrays\interval\__pycache__              |
| .venv\Lib\site-packages\pandas\tests\arrays\masked\__pycache__                |
| .venv\Lib\site-packages\pandas\tests\arrays\numpy_\__pycache__                |
| .venv\Lib\site-packages\pandas\tests\arrays\period\__pycache__                |
| .venv\Lib\site-packages\pandas\tests\arrays\sparse\__pycache__                |
| .venv\Lib\site-packages\pandas\tests\arrays\string_\__pycache__               |
| .venv\Lib\site-packages\pandas\tests\arrays\timedeltas\__pycache__            |
| .venv\Lib\site-packages\pandas\tests\base\__pycache__                         |
| .venv\Lib\site-packages\pandas\tests\computation\__pycache__                  |
| .venv\Lib\site-packages\pandas\tests\config\__pycache__                       |
| .venv\Lib\site-packages\pandas\tests\construction\__pycache__                 |
| .venv\Lib\site-packages\pandas\tests\copy_view\__pycache__                    |
| .venv\Lib\site-packages\pandas\tests\copy_view\index\__pycache__              |
| .venv\Lib\site-packages\pandas\tests\dtypes\__pycache__                       |
| .venv\Lib\site-packages\pandas\tests\dtypes\cast\__pycache__                  |
| .venv\Lib\site-packages\pandas\tests\extension\__pycache__                    |
| .venv\Lib\site-packages\pandas\tests\extension\array_with_attr\__pycache__    |
| .venv\Lib\site-packages\pandas\tests\extension\base\__pycache__               |
| .venv\Lib\site-packages\pandas\tests\extension\date\__pycache__               |
| .venv\Lib\site-packages\pandas\tests\extension\decimal\__pycache__            |
| .venv\Lib\site-packages\pandas\tests\extension\json\__pycache__               |
| .venv\Lib\site-packages\pandas\tests\extension\list\__pycache__               |
| .venv\Lib\site-packages\pandas\tests\frame\__pycache__                        |
| .venv\Lib\site-packages\pandas\tests\frame\constructors\__pycache__           |
| .venv\Lib\site-packages\pandas\tests\frame\indexing\__pycache__               |
| .venv\Lib\site-packages\pandas\tests\frame\methods\__pycache__                |
| .venv\Lib\site-packages\pandas\tests\generic\__pycache__                      |
| .venv\Lib\site-packages\pandas\tests\groupby\__pycache__                      |
| .venv\Lib\site-packages\pandas\tests\groupby\aggregate\__pycache__            |
| .venv\Lib\site-packages\pandas\tests\groupby\methods\__pycache__              |
| .venv\Lib\site-packages\pandas\tests\groupby\transform\__pycache__            |
| .venv\Lib\site-packages\pandas\tests\indexes\__pycache__                      |
| .venv\Lib\site-packages\pandas\tests\indexes\base_class\__pycache__           |
| .venv\Lib\site-packages\pandas\tests\indexes\categorical\__pycache__          |
| .venv\Lib\site-packages\pandas\tests\indexes\datetimelike_\__pycache__        |
| .venv\Lib\site-packages\pandas\tests\indexes\datetimes\__pycache__            |
| .venv\Lib\site-packages\pandas\tests\indexes\datetimes\methods\__pycache__    |
| .venv\Lib\site-packages\pandas\tests\indexes\interval\__pycache__             |
| .venv\Lib\site-packages\pandas\tests\indexes\multi\__pycache__                |
| .venv\Lib\site-packages\pandas\tests\indexes\numeric\__pycache__              |
| .venv\Lib\site-packages\pandas\tests\indexes\object\__pycache__               |
| .venv\Lib\site-packages\pandas\tests\indexes\period\__pycache__               |
| .venv\Lib\site-packages\pandas\tests\indexes\period\methods\__pycache__       |
| .venv\Lib\site-packages\pandas\tests\indexes\ranges\__pycache__               |
| .venv\Lib\site-packages\pandas\tests\indexes\timedeltas\__pycache__           |
| .venv\Lib\site-packages\pandas\tests\indexes\timedeltas\methods\__pycache__   |
| .venv\Lib\site-packages\pandas\tests\indexing\__pycache__                     |
| .venv\Lib\site-packages\pandas\tests\indexing\interval\__pycache__            |
| .venv\Lib\site-packages\pandas\tests\indexing\multiindex\__pycache__          |
| .venv\Lib\site-packages\pandas\tests\interchange\__pycache__                  |
| .venv\Lib\site-packages\pandas\tests\internals\__pycache__                    |
| .venv\Lib\site-packages\pandas\tests\io\__pycache__                           |
| .venv\Lib\site-packages\pandas\tests\io\excel\__pycache__                     |
| .venv\Lib\site-packages\pandas\tests\io\formats\__pycache__                   |
| .venv\Lib\site-packages\pandas\tests\io\formats\style\__pycache__             |
| .venv\Lib\site-packages\pandas\tests\io\json\__pycache__                      |
| .venv\Lib\site-packages\pandas\tests\io\parser\__pycache__                    |
| .venv\Lib\site-packages\pandas\tests\io\parser\common\__pycache__             |
| .venv\Lib\site-packages\pandas\tests\io\parser\dtypes\__pycache__             |
| .venv\Lib\site-packages\pandas\tests\io\parser\usecols\__pycache__            |
| .venv\Lib\site-packages\pandas\tests\io\pytables\__pycache__                  |
| .venv\Lib\site-packages\pandas\tests\io\sas\__pycache__                       |
| .venv\Lib\site-packages\pandas\tests\io\xml\__pycache__                       |
| .venv\Lib\site-packages\pandas\tests\libs\__pycache__                         |
| .venv\Lib\site-packages\pandas\tests\plotting\__pycache__                     |
| .venv\Lib\site-packages\pandas\tests\plotting\frame\__pycache__               |
| .venv\Lib\site-packages\pandas\tests\reductions\__pycache__                   |
| .venv\Lib\site-packages\pandas\tests\resample\__pycache__                     |
| .venv\Lib\site-packages\pandas\tests\reshape\__pycache__                      |
| .venv\Lib\site-packages\pandas\tests\reshape\concat\__pycache__               |
| .venv\Lib\site-packages\pandas\tests\reshape\merge\__pycache__                |
| .venv\Lib\site-packages\pandas\tests\scalar\__pycache__                       |
| .venv\Lib\site-packages\pandas\tests\scalar\interval\__pycache__              |
| .venv\Lib\site-packages\pandas\tests\scalar\period\__pycache__                |
| .venv\Lib\site-packages\pandas\tests\scalar\timedelta\__pycache__             |
| .venv\Lib\site-packages\pandas\tests\scalar\timedelta\methods\__pycache__     |
| .venv\Lib\site-packages\pandas\tests\scalar\timestamp\__pycache__             |
| .venv\Lib\site-packages\pandas\tests\scalar\timestamp\methods\__pycache__     |
| .venv\Lib\site-packages\pandas\tests\series\__pycache__                       |
| .venv\Lib\site-packages\pandas\tests\series\accessors\__pycache__             |
| .venv\Lib\site-packages\pandas\tests\series\indexing\__pycache__              |
| .venv\Lib\site-packages\pandas\tests\series\methods\__pycache__               |
| .venv\Lib\site-packages\pandas\tests\strings\__pycache__                      |
| .venv\Lib\site-packages\pandas\tests\tools\__pycache__                        |
| .venv\Lib\site-packages\pandas\tests\tseries\__pycache__                      |
| .venv\Lib\site-packages\pandas\tests\tseries\frequencies\__pycache__          |
| .venv\Lib\site-packages\pandas\tests\tseries\holiday\__pycache__              |
| .venv\Lib\site-packages\pandas\tests\tseries\offsets\__pycache__              |
| .venv\Lib\site-packages\pandas\tests\tslibs\__pycache__                       |
| .venv\Lib\site-packages\pandas\tests\util\__pycache__                         |
| .venv\Lib\site-packages\pandas\tests\window\__pycache__                       |
| .venv\Lib\site-packages\pandas\tests\window\moments\__pycache__               |
| .venv\Lib\site-packages\pandas\tseries\__pycache__                            |
| .venv\Lib\site-packages\pandas\util\__pycache__                               |
| .venv\Lib\site-packages\pandas\util\version\__pycache__                       |
| .venv\Lib\site-packages\pandas\_config\__pycache__                            |
| .venv\Lib\site-packages\pandas\_libs\__pycache__                              |
| .venv\Lib\site-packages\pandas\_libs\tslibs\__pycache__                       |
| .venv\Lib\site-packages\pandas\_libs\window\__pycache__                       |
| .venv\Lib\site-packages\pandas\_testing\__pycache__                           |
| .venv\Lib\site-packages\pip\__pycache__                                       |
| .venv\Lib\site-packages\pip\_internal\__pycache__                             |
| .venv\Lib\site-packages\pip\_internal\cli\__pycache__                         |
| .venv\Lib\site-packages\pip\_internal\commands\__pycache__                    |
| .venv\Lib\site-packages\pip\_internal\distributions\__pycache__               |
| .venv\Lib\site-packages\pip\_internal\index\__pycache__                       |
| .venv\Lib\site-packages\pip\_internal\locations\__pycache__                   |
| .venv\Lib\site-packages\pip\_internal\metadata\__pycache__                    |
| .venv\Lib\site-packages\pip\_internal\metadata\importlib\__pycache__          |
| .venv\Lib\site-packages\pip\_internal\models\__pycache__                      |
| .venv\Lib\site-packages\pip\_internal\network\__pycache__                     |
| .venv\Lib\site-packages\pip\_internal\operations\__pycache__                  |
| .venv\Lib\site-packages\pip\_internal\operations\build\__pycache__            |
| .venv\Lib\site-packages\pip\_internal\operations\install\__pycache__          |
| .venv\Lib\site-packages\pip\_internal\req\__pycache__                         |
| .venv\Lib\site-packages\pip\_internal\resolution\__pycache__                  |
| .venv\Lib\site-packages\pip\_internal\resolution\legacy\__pycache__           |
| .venv\Lib\site-packages\pip\_internal\resolution\resolvelib\__pycache__       |
| .venv\Lib\site-packages\pip\_internal\utils\__pycache__                       |
| .venv\Lib\site-packages\pip\_internal\vcs\__pycache__                         |
| .venv\Lib\site-packages\pip\_vendor\__pycache__                               |
| .venv\Lib\site-packages\pip\_vendor\cachecontrol\__pycache__                  |
| .venv\Lib\site-packages\pip\_vendor\cachecontrol\caches\__pycache__           |
| .venv\Lib\site-packages\pip\_vendor\certifi\__pycache__                       |
| .venv\Lib\site-packages\pip\_vendor\distlib\__pycache__                       |
| .venv\Lib\site-packages\pip\_vendor\distro\__pycache__                        |
| .venv\Lib\site-packages\pip\_vendor\idna\__pycache__                          |
| .venv\Lib\site-packages\pip\_vendor\msgpack\__pycache__                       |
| .venv\Lib\site-packages\pip\_vendor\packaging\__pycache__                     |
| .venv\Lib\site-packages\pip\_vendor\packaging\licenses\__pycache__            |
| .venv\Lib\site-packages\pip\_vendor\pkg_resources\__pycache__                 |
| .venv\Lib\site-packages\pip\_vendor\platformdirs\__pycache__                  |
| .venv\Lib\site-packages\pip\_vendor\pygments\__pycache__                      |
| .venv\Lib\site-packages\pip\_vendor\pygments\filters\__pycache__              |
| .venv\Lib\site-packages\pip\_vendor\pygments\formatters\__pycache__           |
| .venv\Lib\site-packages\pip\_vendor\pygments\lexers\__pycache__               |
| .venv\Lib\site-packages\pip\_vendor\pygments\styles\__pycache__               |
| .venv\Lib\site-packages\pip\_vendor\pyproject_hooks\__pycache__               |
| .venv\Lib\site-packages\pip\_vendor\pyproject_hooks\_in_process\__pycache__   |
| .venv\Lib\site-packages\pip\_vendor\requests\__pycache__                      |
| .venv\Lib\site-packages\pip\_vendor\resolvelib\__pycache__                    |
| .venv\Lib\site-packages\pip\_vendor\resolvelib\resolvers\__pycache__          |
| .venv\Lib\site-packages\pip\_vendor\rich\__pycache__                          |
| .venv\Lib\site-packages\pip\_vendor\tomli\__pycache__                         |
| .venv\Lib\site-packages\pip\_vendor\tomli_w\__pycache__                       |
| .venv\Lib\site-packages\pip\_vendor\truststore\__pycache__                    |
| .venv\Lib\site-packages\pip\_vendor\urllib3\__pycache__                       |
| .venv\Lib\site-packages\pip\_vendor\urllib3\contrib\__pycache__               |
| .venv\Lib\site-packages\pip\_vendor\urllib3\contrib\emscripten\__pycache__    |
| .venv\Lib\site-packages\pip\_vendor\urllib3\http2\__pycache__                 |
| .venv\Lib\site-packages\pip\_vendor\urllib3\util\__pycache__                  |
| .venv\Lib\site-packages\pkg_resources\__pycache__                             |
| .venv\Lib\site-packages\pkg_resources\extern\__pycache__                      |
| .venv\Lib\site-packages\pkg_resources\_vendor\__pycache__                     |
| .venv\Lib\site-packages\pkg_resources\_vendor\importlib_resources\__pycache__ |
| .venv\Lib\site-packages\pkg_resources\_vendor\jaraco\__pycache__              |
| .venv\Lib\site-packages\pkg_resources\_vendor\jaraco\text\__pycache__         |
| .venv\Lib\site-packages\pkg_resources\_vendor\more_itertools\__pycache__      |
| .venv\Lib\site-packages\pkg_resources\_vendor\packaging\__pycache__           |
| .venv\Lib\site-packages\pkg_resources\_vendor\pyparsing\__pycache__           |
| .venv\Lib\site-packages\pkg_resources\_vendor\pyparsing\diagram\__pycache__   |
| .venv\Lib\site-packages\pluggy\__pycache__                                    |
| .venv\Lib\site-packages\pygments\__pycache__                                  |
| .venv\Lib\site-packages\pygments\filters\__pycache__                          |
| .venv\Lib\site-packages\pygments\formatters\__pycache__                       |
| .venv\Lib\site-packages\pygments\lexers\__pycache__                           |
| .venv\Lib\site-packages\pygments\styles\__pycache__                           |
| .venv\Lib\site-packages\pytest\__pycache__                                    |
| .venv\Lib\site-packages\pytz\__pycache__                                      |
| .venv\Lib\site-packages\scipy\__pycache__                                     |
| .venv\Lib\site-packages\scipy\cluster\__pycache__                             |
| .venv\Lib\site-packages\scipy\cluster\tests\__pycache__                       |
| .venv\Lib\site-packages\scipy\constants\__pycache__                           |
| .venv\Lib\site-packages\scipy\constants\tests\__pycache__                     |
| .venv\Lib\site-packages\scipy\datasets\__pycache__                            |
| .venv\Lib\site-packages\scipy\datasets\tests\__pycache__                      |
| .venv\Lib\site-packages\scipy\fft\__pycache__                                 |
| .venv\Lib\site-packages\scipy\fft\tests\__pycache__                           |
| .venv\Lib\site-packages\scipy\fft\_pocketfft\__pycache__                      |
| .venv\Lib\site-packages\scipy\fft\_pocketfft\tests\__pycache__                |
| .venv\Lib\site-packages\scipy\fftpack\__pycache__                             |
| .venv\Lib\site-packages\scipy\fftpack\tests\__pycache__                       |
| .venv\Lib\site-packages\scipy\integrate\__pycache__                           |
| .venv\Lib\site-packages\scipy\integrate\tests\__pycache__                     |
| .venv\Lib\site-packages\scipy\integrate\_ivp\__pycache__                      |
| .venv\Lib\site-packages\scipy\integrate\_ivp\tests\__pycache__                |
| .venv\Lib\site-packages\scipy\interpolate\__pycache__                         |
| .venv\Lib\site-packages\scipy\interpolate\tests\__pycache__                   |
| .venv\Lib\site-packages\scipy\io\__pycache__                                  |
| .venv\Lib\site-packages\scipy\io\arff\__pycache__                             |
| .venv\Lib\site-packages\scipy\io\arff\tests\__pycache__                       |
| .venv\Lib\site-packages\scipy\io\matlab\__pycache__                           |
| .venv\Lib\site-packages\scipy\io\matlab\tests\__pycache__                     |
| .venv\Lib\site-packages\scipy\io\tests\__pycache__                            |
| .venv\Lib\site-packages\scipy\io\_fast_matrix_market\__pycache__              |
| .venv\Lib\site-packages\scipy\io\_harwell_boeing\__pycache__                  |
| .venv\Lib\site-packages\scipy\io\_harwell_boeing\tests\__pycache__            |
| .venv\Lib\site-packages\scipy\linalg\__pycache__                              |
| .venv\Lib\site-packages\scipy\linalg\tests\__pycache__                        |
| .venv\Lib\site-packages\scipy\misc\__pycache__                                |
| .venv\Lib\site-packages\scipy\misc\tests\__pycache__                          |
| .venv\Lib\site-packages\scipy\ndimage\__pycache__                             |
| .venv\Lib\site-packages\scipy\ndimage\tests\__pycache__                       |
| .venv\Lib\site-packages\scipy\odr\__pycache__                                 |
| .venv\Lib\site-packages\scipy\odr\tests\__pycache__                           |
| .venv\Lib\site-packages\scipy\optimize\__pycache__                            |
| .venv\Lib\site-packages\scipy\optimize\cython_optimize\__pycache__            |
| .venv\Lib\site-packages\scipy\optimize\tests\__pycache__                      |
| .venv\Lib\site-packages\scipy\optimize\_highs\__pycache__                     |
| .venv\Lib\site-packages\scipy\optimize\_lsq\__pycache__                       |
| .venv\Lib\site-packages\scipy\optimize\_shgo_lib\__pycache__                  |
| .venv\Lib\site-packages\scipy\optimize\_trlib\__pycache__                     |
| .venv\Lib\site-packages\scipy\optimize\_trustregion_constr\__pycache__        |
| .venv\Lib\site-packages\scipy\optimize\_trustregion_constr\tests\__pycache__  |
| .venv\Lib\site-packages\scipy\signal\__pycache__                              |
| .venv\Lib\site-packages\scipy\signal\tests\__pycache__                        |
| .venv\Lib\site-packages\scipy\signal\windows\__pycache__                      |
| .venv\Lib\site-packages\scipy\sparse\__pycache__                              |
| .venv\Lib\site-packages\scipy\sparse\csgraph\__pycache__                      |
| .venv\Lib\site-packages\scipy\sparse\csgraph\tests\__pycache__                |
| .venv\Lib\site-packages\scipy\sparse\linalg\__pycache__                       |
| .venv\Lib\site-packages\scipy\sparse\linalg\tests\__pycache__                 |
| .venv\Lib\site-packages\scipy\sparse\linalg\_dsolve\__pycache__               |
| .venv\Lib\site-packages\scipy\sparse\linalg\_dsolve\tests\__pycache__         |
| .venv\Lib\site-packages\scipy\sparse\linalg\_eigen\__pycache__                |
| .venv\Lib\site-packages\scipy\sparse\linalg\_eigen\arpack\__pycache__         |
| .venv\Lib\site-packages\scipy\sparse\linalg\_eigen\arpack\tests\__pycache__   |
| .venv\Lib\site-packages\scipy\sparse\linalg\_eigen\lobpcg\__pycache__         |
| .venv\Lib\site-packages\scipy\sparse\linalg\_eigen\lobpcg\tests\__pycache__   |
| .venv\Lib\site-packages\scipy\sparse\linalg\_eigen\tests\__pycache__          |
| .venv\Lib\site-packages\scipy\sparse\linalg\_isolve\__pycache__               |
| .venv\Lib\site-packages\scipy\sparse\linalg\_isolve\tests\__pycache__         |
| .venv\Lib\site-packages\scipy\sparse\tests\__pycache__                        |
| .venv\Lib\site-packages\scipy\spatial\__pycache__                             |
| .venv\Lib\site-packages\scipy\spatial\tests\__pycache__                       |
| .venv\Lib\site-packages\scipy\spatial\transform\__pycache__                   |
| .venv\Lib\site-packages\scipy\spatial\transform\tests\__pycache__             |
| .venv\Lib\site-packages\scipy\special\__pycache__                             |
| .venv\Lib\site-packages\scipy\special\tests\__pycache__                       |
| .venv\Lib\site-packages\scipy\special\tests\data\__pycache__                  |
| .venv\Lib\site-packages\scipy\special\_precompute\__pycache__                 |
| .venv\Lib\site-packages\scipy\stats\__pycache__                               |
| .venv\Lib\site-packages\scipy\stats\tests\__pycache__                         |
| .venv\Lib\site-packages\scipy\stats\tests\data\__pycache__                    |
| .venv\Lib\site-packages\scipy\stats\_boost\__pycache__                        |
| .venv\Lib\site-packages\scipy\stats\_levy_stable\__pycache__                  |
| .venv\Lib\site-packages\scipy\stats\_rcont\__pycache__                        |
| .venv\Lib\site-packages\scipy\stats\_unuran\__pycache__                       |
| .venv\Lib\site-packages\scipy\_lib\__pycache__                                |
| .venv\Lib\site-packages\scipy\_lib\array_api_compat\__pycache__               |
| .venv\Lib\site-packages\scipy\_lib\array_api_compat\common\__pycache__        |
| .venv\Lib\site-packages\scipy\_lib\array_api_compat\cupy\__pycache__          |
| .venv\Lib\site-packages\scipy\_lib\array_api_compat\numpy\__pycache__         |
| .venv\Lib\site-packages\scipy\_lib\array_api_compat\torch\__pycache__         |
| .venv\Lib\site-packages\scipy\_lib\tests\__pycache__                          |
| .venv\Lib\site-packages\scipy\_lib\_uarray\__pycache__                        |
| .venv\Lib\site-packages\setuptools\__pycache__                                |
| .venv\Lib\site-packages\setuptools\command\__pycache__                        |
| .venv\Lib\site-packages\setuptools\config\__pycache__                         |
| .venv\Lib\site-packages\setuptools\config\_validate_pyproject\__pycache__     |
| .venv\Lib\site-packages\setuptools\extern\__pycache__                         |
| .venv\Lib\site-packages\setuptools\_distutils\__pycache__                     |
| .venv\Lib\site-packages\setuptools\_distutils\command\__pycache__             |
| .venv\Lib\site-packages\setuptools\_vendor\__pycache__                        |
| .venv\Lib\site-packages\setuptools\_vendor\importlib_metadata\__pycache__     |
| .venv\Lib\site-packages\setuptools\_vendor\importlib_resources\__pycache__    |
| .venv\Lib\site-packages\setuptools\_vendor\jaraco\__pycache__                 |
| .venv\Lib\site-packages\setuptools\_vendor\jaraco\text\__pycache__            |
| .venv\Lib\site-packages\setuptools\_vendor\more_itertools\__pycache__         |
| .venv\Lib\site-packages\setuptools\_vendor\packaging\__pycache__              |
| .venv\Lib\site-packages\setuptools\_vendor\pyparsing\__pycache__              |
| .venv\Lib\site-packages\setuptools\_vendor\pyparsing\diagram\__pycache__      |
| .venv\Lib\site-packages\setuptools\_vendor\tomli\__pycache__                  |
| .venv\Lib\site-packages\tabulate\__pycache__                                  |
| .venv\Lib\site-packages\tzdata\__pycache__                                    |
| .venv\Lib\site-packages\tzdata\zoneinfo\__pycache__                           |
| .venv\Lib\site-packages\tzdata\zoneinfo\Africa\__pycache__                    |
| .venv\Lib\site-packages\tzdata\zoneinfo\America\__pycache__                   |
| .venv\Lib\site-packages\tzdata\zoneinfo\America\Argentina\__pycache__         |
| .venv\Lib\site-packages\tzdata\zoneinfo\America\Indiana\__pycache__           |
| .venv\Lib\site-packages\tzdata\zoneinfo\America\Kentucky\__pycache__          |
| .venv\Lib\site-packages\tzdata\zoneinfo\America\North_Dakota\__pycache__      |
| .venv\Lib\site-packages\tzdata\zoneinfo\Antarctica\__pycache__                |
| .venv\Lib\site-packages\tzdata\zoneinfo\Arctic\__pycache__                    |
| .venv\Lib\site-packages\tzdata\zoneinfo\Asia\__pycache__                      |
| .venv\Lib\site-packages\tzdata\zoneinfo\Atlantic\__pycache__                  |
| .venv\Lib\site-packages\tzdata\zoneinfo\Australia\__pycache__                 |
| .venv\Lib\site-packages\tzdata\zoneinfo\Brazil\__pycache__                    |
| .venv\Lib\site-packages\tzdata\zoneinfo\Canada\__pycache__                    |
| .venv\Lib\site-packages\tzdata\zoneinfo\Chile\__pycache__                     |
| .venv\Lib\site-packages\tzdata\zoneinfo\Etc\__pycache__                       |
| .venv\Lib\site-packages\tzdata\zoneinfo\Europe\__pycache__                    |
| .venv\Lib\site-packages\tzdata\zoneinfo\Indian\__pycache__                    |
| .venv\Lib\site-packages\tzdata\zoneinfo\Mexico\__pycache__                    |
| .venv\Lib\site-packages\tzdata\zoneinfo\Pacific\__pycache__                   |
| .venv\Lib\site-packages\tzdata\zoneinfo\US\__pycache__                        |
| .venv\Lib\site-packages\yaml\__pycache__                                      |
| .venv\Lib\site-packages\_distutils_hack\__pycache__                           |
| .venv\Lib\site-packages\_pytest\__pycache__                                   |
| .venv\Lib\site-packages\_pytest\assertion\__pycache__                         |
| .venv\Lib\site-packages\_pytest\config\__pycache__                            |
| .venv\Lib\site-packages\_pytest\mark\__pycache__                              |
| .venv\Lib\site-packages\_pytest\_code\__pycache__                             |
| .venv\Lib\site-packages\_pytest\_io\__pycache__                               |
| .venv\Lib\site-packages\_pytest\_py\__pycache__                               |
| .venv\Lib\site-packages\_yaml\__pycache__                                     |
| .venv                                                                         |

## Artifact manifest sample

| artifact                                   |   size_bytes | sha256_12    |
|:-------------------------------------------|-------------:|:-------------|
| README.md                                  |         5889 | 8116f728fa51 |
| PROJECT_CARD.md                            |         3308 | f54b750fd387 |
| Makefile                                   |          544 | 9aea53b0963c |
| pyproject.toml                             |          272 | 72a0ebedfc7e |
| requirements.txt                           |          101 | 8dc69e0b4cbe |
| Dockerfile                                 |          335 | 933fbe21fb17 |
| .dockerignore                              |          105 | cfa93e19df4d |
| .gitignore                                 |           72 | 4951c9396d99 |
| configs\backtesting_config.yaml            |           58 | 8baec97a908e |
| configs\model_inventory.yaml               |         1416 | 312d84d78b51 |
| configs\monte_carlo_config.yaml            |          120 | 1199a1278c11 |
| configs\numerical_tolerance.yaml           |          185 | a9b71a49a5e7 |
| configs\pricing_config.yaml                |          229 | d61babe565cc |
| configs\release_gates.yaml                 |          200 | 3040ef6687e2 |
| configs\stress_config.yaml                 |          439 | bbdad6dfcbe6 |
| configs\validation_thresholds.yaml         |          298 | 59090f03a323 |
| src\__init__.py                            |            0 | e3b0c44298fc |
| src\benchmarks\__init__.py                 |            0 | e3b0c44298fc |
| src\benchmarks\finite_difference_checks.py |          374 | a5f963501acb |
| src\dashboard\__init__.py                  |            0 | e3b0c44298fc |

## Local run commands

`python scripts/run_pipeline.py`, `pytest -q`, `make run`, `make test`.

## CI recommendation

GitHub Actions workflow included under `.github/workflows/ci.yml`; outputs/reports can be regenerated locally.
