%define prj    Text_reST

%define xmldir  %{_var}/lib/pear
%define peardir %(pear config-get php_dir 2> /dev/null)

Name:          horde-text-rest
Version:       0.0.2
Release:       14
Summary:       REStructuredText parser and formatters
License:       LGPL
Group:         Networking/Mail
Url:           https://pear.horde.org/index.php?package=%{prj}
Source0:       %{prj}-%{version}.tgz
BuildArch:     noarch
Requires(pre): php-pear
Requires:      php-pear
Requires:      php-pear-channel-horde
BuildRequires: php-pear
BuildRequires: php-pear-channel-horde

%description
This package provides a parser for reStructguredText and reformatters
for different output formats.


%prep
%setup -q -n %{prj}-%{version}

%build
%__mv ../package.xml .

%install
pear install --packagingroot %{buildroot} --nodeps package.xml

%__rm -rf %{buildroot}/%{peardir}/.{filemap,lock,registry,channels,depdb,depdblock}

%__mkdir_p %{buildroot}%{xmldir}
%__cp package.xml %{buildroot}%{xmldir}/%{prj}.xml

%clean
%__rm -rf %{buildroot}

%post
pear install --nodeps --soft --force --register-only %{xmldir}/%{prj}.xml

%postun
if [ "$1" -eq "0" ]; then
  pear uninstall --nodeps --ignore-errors --register-only pear.horde.org/%{prj}
fi

%files
%defattr(-, root, root)
%{xmldir}/%{prj}.xml
%dir %{peardir}/Text
%dir %{peardir}/Text/reST
%dir %{peardir}/Text/reST/Formatter
%{peardir}/Text/reST.php
%{peardir}/Text/reST/Formatter.php
%{peardir}/Text/reST/Formatter/html.php
%{peardir}/Text/reST/Parser.php
%dir %{peardir}/tests/Text_reST
%dir %{peardir}/tests/Text_reST/tests
%{peardir}/tests/Text_reST/tests/headings.phpt
%{peardir}/tests/Text_reST/tests/lblocks.phpt
%{peardir}/tests/Text_reST/tests/links.phpt
%{peardir}/tests/Text_reST/tests/roles.phpt




%changelog
* Sat Jul 31 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.2-13mdv2011.0
+ Revision: 564103
- Increased release for rebuild

* Thu Mar 18 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.2-12mdv2010.1
+ Revision: 524787
- replaced Requires(pre): %%{_bindir}/pear with Requires(pre): php-pear
  increased release version

* Sun Feb 21 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.2-1mdv2010.1
+ Revision: 508865
- replace PreRequ with Requires(pre)
- import horde-text-rest


