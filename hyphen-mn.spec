Name: hyphen-mn
Summary: Mongolian hyphenation rules
%define upstreamid 20100531
Version: 0.%{upstreamid}
Release: 5%{?dist}
Source: http://tug.org/svn/texhyphen/trunk/hyph-utf8/tex/generic/hyph-utf8/patterns/tex/hyph-mn-cyrl.tex?view=co#/hyph-mn-cyrl.tex
Group: Applications/Text
URL: http://www.ctan.org/tex-archive/help/Catalogue/entries/mnhyphn.html
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: LPPL
BuildArch: noarch
BuildRequires: hyphen-devel
Requires: hyphen
Patch0: hyphen-mn-cleantex.patch

%description
Mongolian hyphenation rules.

%prep
%setup -T -q -c -n hyphen-mn
cp -p %{SOURCE0} .
%patch0 -p0 -b .clean

%build
substrings.pl hyph-mn-cyrl.tex hyph_mn_MN.dic UTF-8
echo "Created with substring.pl by substrings.pl hyph-mn-cyrl.tex hyph_mn_MN.dic UTF-8" > README
echo "Original in-line credits were:" >> README
echo "" >> README
head -n 83 hyph-mn-cyrl.tex >> README

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_mn_MN.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README
%{_datadir}/hyphen/*

%changelog
* Thu Jan 31 2013 Caolán McNamara <caolanm@redhat.com> - 0.20100531-5
- Resolves: rhbz#905980 rework for new link

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20100531-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20100531-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20100531-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jun 01 2010 Caolán McNamara <caolanm@redhat.com> - 0.20100531-1
- latest version

* Sun Apr 11 2010 Caolán McNamara <caolanm@redhat.com> - 0.20100406-1
- latest version

* Thu Nov 05 2009 Caolán McNamara <caolanm@redhat.com> - 0.20091104-1
- latest version

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20090315-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Mar 16 2009 Caolán McNamara <caolanm@redhat.com> - 0.20090315-1
- initial version
