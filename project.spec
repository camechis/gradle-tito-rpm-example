Name:		example		
Version:	1.1.0	
Release:	1%{?dist}
Summary: 	example	

License:	Apache 2	


%description


%prep


%build
./gradlew build

%install


%clean


%files



%changelog
* Sun Sep 29 2013 Travis Camechis <camechis@gail.com> 1.1.0-1
- new package built with tito


