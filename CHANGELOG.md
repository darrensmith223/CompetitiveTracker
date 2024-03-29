# Change Log
All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/).

## [1.1.0] - 2022-02-22
### Added
- Updated authentication mechanism to leverage authentication header

### Fixed
- Bug that resulted in "path not found" error in core.domains.get_all_domains() 
- Minor documentation errors for ease of use

## [1.0.1] - 2022-02-11
### Fixed
- Bug that prevented domains parameter from being passed in get_brand_volume_and_esps() for lists smaller than 300 

## [1.0.0] - 2021-06-02
### Added
- Base competitivetracker class
- Core competitivetracker class
- Domain_info competitivetracker class
- Intelligence competitivetracker class
- Overlaps competitivetracker class
- Ping competitivetracker class
- Search competitivetracker class
- Docs on readthedocs.org