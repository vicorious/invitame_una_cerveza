import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { EleccionComponentComponent } from './eleccion-component.component';

describe('EleccionComponentComponent', () => {
  let component: EleccionComponentComponent;
  let fixture: ComponentFixture<EleccionComponentComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ EleccionComponentComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(EleccionComponentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
