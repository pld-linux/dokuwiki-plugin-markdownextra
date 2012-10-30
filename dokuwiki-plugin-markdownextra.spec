%define		plugin	markdownextra
%define		php_min_version 5.0.0
%include	/usr/lib/rpm/macros.php
Summary:	DokuWiki Markdown Extra plugin
Name:		dokuwiki-plugin-%{plugin}
Version:	20101106
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://madpropellerhead.com/projects/markdownextra.tgz
# Source0-md5:	3e703cbfe84108e252c354009a304cd2
URL:		http://www.dokuwiki.org/plugin:markdownextra
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.553
Requires:	dokuwiki >= 20091225
Requires:	php-common >= 4:%{php_min_version}
Requires:	php-markdown-extra >= 1.2.4
Requires:	php-pcre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokuconf	/etc/webapps/dokuwiki
%define		dokudir		/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}
%define		find_lang 	%{_usrlibrpm}/dokuwiki-find-lang.sh %{buildroot}

%description
Parses PHP Markdown Extra blocks.

%prep
%setup -qc
mv %{plugin}/* .
%undos -f txt,php

version=$(awk '/^date/{print $2}' plugin.info.txt)
if [ "$(echo "$version" | tr -d -)" != %{version} ]; then
	: %%{version} mismatch
	exit 1
fi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}
%{__rm} $RPM_BUILD_ROOT%{plugindir}/License.text

# php-markdown-extra
%{__rm} $RPM_BUILD_ROOT%{plugindir}/markdown.php

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc License.text
%dir %{plugindir}
%{plugindir}/*.php
%{plugindir}/*.txt
