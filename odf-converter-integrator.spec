Summary:	Convert Office 2007 (OOXML) files for OpenOffice.org
Summary(pl.UTF-8):	Convert Office 2007 (OOXML) files for OpenOffice.org
Name:		odf-converter-integrator
Version:	0.1.5
Release:	0.1
License:	GPL v3
Group:		Applications
Source0:	http://katana.oooninja.com/f/software/%{name}-source-%{version}.tar.bz2
URL:		http://katana.oooninja.com/w/odf-converter-integrator
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A utility to convert Microsoft Office 2007 (Office Open XML) files and
automatically start OpenOffice.org. Registers file types and mime
types such as .docx, .xlsx, and .pptx so that Nautilus, Firefox, and
other programs automatically recognize them.

%description -l pl.UTF-8
A utility to convert Microsoft Office 2007 (Office Open XML) files and
automatically start OpenOffice.org. Registers file types and mime
types such as .docx, .xlsx, and .pptx so that Nautilus, Firefox, and
other programs automatically recognize them.


%prep
%setup -q -n %{name}-source-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir},%{_datadir}/mime/packages,%{_datadir}/mimelnk/application}
install linux/%{name}-%{version}/%{_bindir}/%{name} $RPM_BUILD_ROOT%{_bindir}
install linux/%{name}-%{version}%{_desktopdir}/*.desktop $RPM_BUILD_ROOT%{_desktopdir}
install linux/%{name}-%{version}%{_datadir}/mime/packages/%{name}.xml $RPM_BUILD_ROOT%{_datadir}/mime/packages/
install linux/%{name}-%{version}%{_datadir}/mimelnk/application/%{name}*.desktop $RPM_BUILD_ROOT%{_datadir}/mimelnk/application

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post
%update_mime_database

%postun
%update_desktop_database_postun
%update_mime_database

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/odf-converter-integrator-*.desktop
%{_datadir}/mime/packages/odf-converter-integrator.xml
%{_datadir}/mimelnk/application/odf-converter-integrator-*.desktop
