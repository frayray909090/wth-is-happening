using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace Store_WPF
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }
        void UIElement_OnMouseDown(object sender, MouseButtonEventArgs e)
        {
            this.DragMove();
        }
        void Close_OnMouseDown(object sender, MouseButtonEventArgs e)
        {
            Close();
        }
        void Home(object sender, MouseButtonEventArgs e)
        {
            Close();
        }
        void Featured(object sender, MouseButtonEventArgs e)
        {
            Close();
        }
        void Mine(object sender, MouseButtonEventArgs e)
        {
            Close();
        }
        void Malware(object sender, MouseButtonEventArgs e)
        {
            Close();
        }
        void Other(object sender, MouseButtonEventArgs e)
        {
            Close();
        }
    }
}
